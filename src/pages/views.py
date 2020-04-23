from django.shortcuts import render
from django.http import HttpResponse
from item.models import entry


# Create your views here.
def home_view(request):
    entries = entry.objects.all()
    return render(request, "home.html", {'item': entries})


def contact_view(request):
    return render(request, "contact.html", {})


def about_view(request):
    return render(request, "about.html", {})
