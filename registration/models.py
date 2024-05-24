from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class RegistrationForm(models.Model):
    # Define maximum lengths and other properties for first and last names
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # Mobile number is unique to ensure each registration is linked to a unique phone number
    mobile_number = models.CharField(max_length=15, unique=True)

    # Choices for gender using a tuple of tuples
    GENDER_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    # Password field; ensure it uses proper hashing and storage practices
    password = models.CharField(max_length=128)

    # Confirm password field; used for validation only, should not be stored
    confirm_password = models.CharField(max_length=128, blank=True)

    # Optional field for additional comments from the user
    comment = models.TextField(blank=True, null=True)
    
    # Meta class to define database table name and possibly other options like ordering
    class Meta:
        db_table = "registrationForm"

