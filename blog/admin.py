from django.contrib import admin
from .models import Actors, Movies, Directors

admin.site.register(Actors)
admin.site.register(Movies)
admin.site.register(Directors)
