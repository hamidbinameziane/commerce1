from django.contrib import admin

from .models import listing, bid, comment

# Register your models here.
admin.site.register(listing)
admin.site.register(bid)
admin.site.register(comment)
