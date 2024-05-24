# Import admin module from Django's contrib package
from django.contrib import admin
# Import the RegistrationForm model from the current app's models module
from .models import RegistrationForm

# This script customizes the Django admin interface

# Register the RegistrationForm model to make it available in the admin interface
admin.site.register(RegistrationForm)

