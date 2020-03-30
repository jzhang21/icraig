from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Listing
from .models import Profile


admin.site.register(Listing)
admin.site.register(Profile)