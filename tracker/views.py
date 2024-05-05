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
    # Logic to fetch and process transaction data from the database
    # You can replace this with your actual logic to fetch transaction data
    transaction = [
        {'date': '2024-05-01', 'description': 'Transaction 1', 'amount': 100},
        {'date': '2024-05-02', 'description': 'Transaction 2', 'amount': -50},
        # Add more transaction data as needed
    ]

    return render(request, 'transaction.html', {'transaction': transaction})


def budgeting(request):
    return render(request, 'budgeting.html')


def financial(request):
    return render(request, 'financial.html')


def analysis(request):
    return render(request, 'analysis.html')


def settings(request):
    return render(request, 'settings.html')


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
