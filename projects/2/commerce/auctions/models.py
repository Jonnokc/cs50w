from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    name = models.CharField(max_length=40)
    asking_price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=300)


    def __str__(self):
        return f"{self.name} {self.asking_price} {self.description}"


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    item = models.ManyToManyField(Listing, blank=True, related_name='comment_item')
    description = models.CharField(max_length=300)


    def __str__(self):
        return f"{self.username} {self.description}"


class Bid(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bid_item')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='bidder')
    bid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.item} {self.bid_amount} {self.bid_time}"


class Watchlist(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='watch_item')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watcher')
