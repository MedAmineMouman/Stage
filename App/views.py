from django.shortcuts import render

def example_page(request):
    return render(request, 'login.html')
