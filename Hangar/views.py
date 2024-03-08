from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def terms_and_conditions(request):
    # View logic
    return render(request, 'tc.html')

def shop_view(request):
    # Logic to handle requests to the "/shop" URL
    return render(request, 'basic.html')