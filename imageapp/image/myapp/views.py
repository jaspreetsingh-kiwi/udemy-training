from django.shortcuts import render, redirect
from .forms import ImageForm
from django.contrib import messages

from .models import Image


# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if Image.objects.filter(company_image=f"myimage/{request.FILES.get('company_image')}").exists():
            messages.error(request, "already exists")
        elif form.is_valid():
            form.save()
    form = ImageForm()

    return render(request, 'myapp/home.html', {'form': form})


# Read operation
def display(request):
    queryset = Image.objects.all()
    print(queryset)
    context = {"key1": queryset}
    return render(request, "myapp/display.html", context)


# Update/Edit Data
def update_data(request, id):
    if request.method == 'POST':
        pi = Image.objects.get(pk=id)
        form = ImageForm(request.POST, request.FILES,instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = Image.objects.get(pk=id)
        form = ImageForm(instance=pi)
    return render(request, 'myapp/update.html', {'form': form})


# Delete Operation
def delete_data(request, id):
    if request.method == 'POST':
        pi = Image.objects.get(pk=id)
        pi.delete()
        return redirect('/')
