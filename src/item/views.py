from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import entry
from .forms import EntryForm


# Create your views here.
def add_item_view(request):
    form = EntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EntryForm()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "addItem.html", context)


# def item_create_view(request):
#     my_form = RawEntryForm(request.GET)
#     if request.method == "POST":
#         my_form = RawEntryForm(request.POST)
#         if my_form.is_valid():
#             #Now the data is good
#             print(my_form.cleaned_data)
#             entry.objects.create(**my_form.cleaned_data)
#     context = {
#         "form": my_form
#     }
#     return render(request, "addItem.html", context)

def delete_item_view(request):
    return render(request, "deleteItem.html", {})
