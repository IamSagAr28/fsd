from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignupForm

class ProfileView(View):
    """Class-based view for handling user profiles."""
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'users/profile.html')

@login_required
def profile_view(request):
    """View for displaying the user's profile."""
    return render(request, 'users/profile.html')

# Simplified dashboard view for demo purposes
def dashboard_view(request):
    # For the simplified demo, we don't need to fetch any data
    # Just render the template with static content
    return render(request, 'dashboard/dashboard.html')

# Simplified courses view for demo purposes
def courses_view(request):
    # For the simplified demo, we don't need to fetch any data
    # Just render the template with static content
    return render(request, 'courses/courses.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                # Redirect to the requested page or dashboard
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

def signup_view(request):
    try:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"Account created for {username}! You can now log in.")
                return redirect('account_login')
            else:
                # Print form errors to server console for debugging
                print(f"Form errors: {form.errors}")
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        else:
            form = SignupForm()
        
        return render(request, 'users/signup.html', {'form': form})
    except Exception as e:
        # Print the exception for debugging
        import traceback
        print(f"Exception in signup_view: {e}")
        print(traceback.format_exc())
        messages.error(request, f"An error occurred: {e}")
        form = SignupForm()
        return render(request, 'users/signup.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')
