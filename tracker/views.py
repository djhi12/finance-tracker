from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import pandas as pd
import matplotlib.pyplot as plt
# import mpld3
import numpy as np
import io
import urllib
import base64


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    # Example income and expenses data
    income_data = [1000, 1500, 2000, 1800, 1200]
    expenses_data = [500, 700, 800, 1000, 600]

    # Calculate total income, total expenses, and current balance
    total_income = sum(income_data)
    total_expenses = sum(expenses_data)
    current_balance = total_income - total_expenses

    # Plotting the income vs expenses graph
    plt.figure(figsize=(8, 4))
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    plt.plot(months, income_data, label='Income', marker='o')
    plt.plot(months, expenses_data, label='Expenses', marker='x')
    plt.title('Income vs Expenses')
    plt.xlabel('Months')
    plt.ylabel('Amount')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Convert plot to PNG image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Embedding the PNG image into HTML
    graph_url = base64.b64encode(buffer.getvalue()).decode('utf-8')
    graph_html = f'<img src="data:image/png;base64,{graph_url}" />'

    # Context data to pass to the template
    context = {
        'total_income': total_income,
        'current_balance': current_balance,
        'graph': graph_html,  # Pass the HTML containing the image to the template
    }

    return render(request, 'dashboard.html', context)


def overview(request):
    return render(request, 'overview.html')


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
    # Create your Matplotlib plot
    # fig, ax = plt.subplots()
    # ax.plot([1, 2, 3, 4], [10, 20, 25, 30],
    #         linestyle='--', marker='o', color='b')

    # # Convert the plot to HTML
    # html = mpld3.fig_to_html(fig)

    # Render the 'transactions.html' template with the plot HTML included
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
