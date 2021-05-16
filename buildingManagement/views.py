from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "buildingManagement/home.html")

def stock(request):
    return render(request, "buildingManagement/stock.html")

def reports(request):
    return render(request, "buildingManagement/reports.html")

def contact(request):
    return render(request, "buildingManagement/contact.html")