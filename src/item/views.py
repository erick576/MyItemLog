import csv

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import entry
from .forms import EntryForm


# @permission_required('admin.can_add_log_entry')
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

# @permission_required('admin.can_add_log_entry')
def delete_item_view(request, id):
    obj = get_object_or_404(entry, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context = {
        "object": obj
    }
    return render(request, "deleteItem.html", context)


# @permission_required('admin.can_add_log_entry')
def delete_all_item_view(request):
    if request.method == "POST":
        entry.objects.all().delete()
        return redirect('/')
    return render(request, "deleteAll.html")


# @permission_required('admin.can_add_log_entry')
def edit_item_view(request, id):
    instance = get_object_or_404(entry, id=id)
    form = EntryForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            instance.save()
            form = EntryForm()
            return redirect('/')
    context = {
        "form": form,
        "object": instance
    }
    return render(request, "editItem.html", context)


# @permission_required('admin.can_add_log_entry')
def entry_download(self):
    items = entry.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="items.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['Item', 'Picture_URL', 'Description', 'Price', 'Date', 'URL'])

    for obj in items:
        writer.writerow([obj.Item, obj.Picture_URL, obj.Description, obj.Price, obj.Date, obj.URL])
    return response
