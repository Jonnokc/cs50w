from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


# The default route of your web application should let users view
# all of the currently active auction listings. For each active listing, this page should
# display (at minimum) the title, description, current price, and photo (if one exists for the listing).

# def flight(request, flight_id):
#     flight = Flight.objects.get(id=flight_id)
#
#     return render(request, "flights/flight.html", {
#         "flight": flight,
#         "passengers": flight.passengers.all(),
#         "non_passengers": Passenger.objects.exclude(flights=flight).all()
#     })

# def flight(request, flight_id):
#     flight = Flight.objects.get(id=flight_id)
#     passengers = flight.passengers.all()
#     return render(request, "flights/flight.html", {
#         "flight": flight,
#         "passengers": passengers
#     })

# AuthorizedEmail.objects.aggregate(Max('added'))


def index(request):
    # listings = Listing.objects.all()
    # bids = Bid.objects.all()

    return render(request, "auctions/index.html", {
        "listings": 'listings',
        # "bids": bids

    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
