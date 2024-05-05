from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def transaction(request):
    return render(request, 'transaction.html')


def dashboard(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Authentication failed
            return render(request, 'dashboard.html', {'error': 'Invalid email or password'})

    # Render the dashboard template after successful login
    return render(request, 'dashboard.html')


@login_required
def edit_details(request):
    if request.method == 'POST':
        # Get form data
        email = request.POST.get('email')
        # Update user details
        request.user.email = email
        request.user.save()
        # Redirect back to the dashboard
        return redirect('dashboard')
    else:
        # If not a POST request, render the edit details form
        return render(request, 'edit_details.html')
