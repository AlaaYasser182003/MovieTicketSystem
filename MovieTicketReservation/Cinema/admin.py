from django.contrib import admin
from .models import Movie, Showtime, reservations, Seat,Payment

# Register your models here.

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Seat)
admin.site.register(reservations)
admin.site.register(Payment)
