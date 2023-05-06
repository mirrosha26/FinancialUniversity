from django.contrib import admin
from .models import Genre, Director, Actor, Movie, Client, Order, Review

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre', 'director')
    list_filter = ('genre', 'director')
    search_fields = ('title', 'description', 'genre__name', 'director__first_name', 'director__last_name')

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Review)
