from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import *
#main view of homepage
def home(request):
    #if user is trying to filter cars
    if request.method == "POST":
        color = request.POST.get('color')
        print(color)
        cars = Cars.objects.filter(color=color)
    else:
        cars = Cars.objects.all()
    #return all filtered/unfiltered cars
    form = CarsForm()
    filter_form = FilterForm() 
    return render(request, 'home.html', {'cars':cars, 'form':form, 'filter_form': filter_form})

#add car logic
def add_car(request):
    cars = Cars.objects.all()
    if request.method == "POST":
        form = CarsForm(request.POST)
        name = request.POST.get('name')
        color = request.POST.get('color')
        car = Cars(
            name = name,
            color = color
            )
        car.save()
    #automatically redirects back to home
    return redirect('home')


