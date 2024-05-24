from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from registration.models import RegistrationForm
from django.contrib.auth.hashers import make_password

# View for the home page
def about_us(request):
    # Render the home page template
    return render(request, "index.html")

# View for the About Us page
def activities(request):
    # Render the activities page template
    return render(request, "activities.html")

# View for the Modules page
def modules(request):
    # Render the modules page template
    return render(request, "modules.html")

# View for the Registration page
def registration(request):
    # Render the registration page template
    return render(request, "registration.html")

# Function to handle user registration
def insertUser(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')
        comment = request.POST.get('comment')

        try:
            if password == con_password:
                # Create a hashed password
                hashed_password = make_password(password)
                con_hashed_password = make_password(con_password)
                
                # Create a user instance with the hashed passwords
                user = RegistrationForm(
                    first_name=fname, 
                    last_name=lname, 
                    mobile_number=mobile, 
                    gender=gender, 
                    password=hashed_password,
                    confirm_password=con_hashed_password,
                    comment=comment
                )
                
                # Save the user instance to the database
                user.save()
                # Display success message and redirect to the registration page
                messages.success(request, 'Registration successful!')
                return redirect("registration")
            else:
                # Display error message if passwords do not match
                messages.error(request, 'Passwords do not match.')
        except IntegrityError:
            # Display error message if the mobile number is already in use
            messages.error(request, 'Mobile number is already in use. Please choose a different one.')
    
    # Redirect to the registration page if not POST or if there are errors
    return redirect('registration')
