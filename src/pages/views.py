from django.shortcuts import render, redirect
from django.http import HttpResponse
from item.models import entry
from django.db.models import Q


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        entries = entry.objects.filter(user=request.user)
        return render(request, "home.html", {'item': entries})
    else:
        return render(request, "home.html")


def contact_view(request):
    return render(request, "contact.html", {})


def about_view(request):
    return render(request, "about.html", {})


def profile_view(request):
    return render(request, "profile.html", {})


def home_search(request):
    query = request.GET.get('q')
    if query.isspace():
        return redirect('/')
    if query:
        results = entry.objects.filter(user=request.user) & entry.objects.filter(Q(Item__icontains=query) | Q(Price__icontains=query) | Q(Date__icontains=query))
    else:
        return redirect('/')
    context = {
        "object_list": results
    }
    return render(request, 'homeSearch.html', context)
