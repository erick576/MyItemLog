from django.shortcuts import render, redirect
from django.http import HttpResponse
from item.models import entry
from django.db.models import Q


# Create your views here.
def home_view(request):
    entries = entry.objects.all()
    return render(request, "home.html", {'item': entries})


def contact_view(request):
    return render(request, "contact.html", {})


def about_view(request):
    return render(request, "about.html", {})


def home_search(request):
    query = request.GET.get('q')
    if query.isspace():
        return redirect('/')
    if query:
        results = entry.objects.filter(Q(Item__icontains=query) | Q(Price__icontains=query) | Q(Date__icontains=query))
    else:
        return redirect('/')
    context = {
        "object_list": results
    }
    return render(request, 'homeSearch.html', context)
