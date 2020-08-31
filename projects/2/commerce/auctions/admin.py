from django.contrib import admin

from .models import *


class BidAdmin(admin.ModelAdmin):
    list_display = ('listing_name', 'user', 'bid_amount', 'bid_time')

    # yeah.... this here is not in any of the documentation or in the lecture. -_-
    def listing_name(self, obj):
        return obj.item.name

    # returns specific listing name from foreign key
    listing_name.admin_order_field = 'name'


admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Bid, BidAdmin)
admin.site.register(Watchlist)
admin.site.register(Listing)
