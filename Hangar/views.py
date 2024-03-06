from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def terms_and_conditions(request):
    # View logic
    return render(request, 'tc.html')