from django.shortcuts import render

def index(request):
    return render(request, "solarpv/index.html") 

def dashboard(request):
    return render(request, "solarpv/dashboard.html")

def client(request):
    return render(request, "solarpv/client.html")

def product(request):
    return render(request, "solarpv/product.html")

def location(request):
    return render(request, "solarpv/location.html")

def certificate(request):
    return render(request, "solarpv/certificate.html")

def test_standard(request):
    return render(request, "solarpv/test_standard.html")
