from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import JsonResponse


def index(request):
    data = {
        'title': 'Главная страница',
        'form': 'form',
    }
    return render(request, 'progruz/index.html', data)


def about(request):
    return render(request, 'progruz/about.html')


def contacts(request):
    return render(request, 'progruz/contacts.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def price(request):
    if request.method == 'POST':
        hours = int(request.POST.get('hours', 0))
        loaders = int(request.POST.get('loaders', 0))

        truck_price = 80
        loader_price = 11

        truck_cost = hours * truck_price
        loaders_cost = loaders * loader_price
        total_cost = truck_cost + loaders_cost

        discount_amount = 0
        if total_cost > 500:
            discount_amount = total_cost * 0.1

        final_price = total_cost - discount_amount

        return JsonResponse({
            'truck_cost': truck_cost,
            'loaders_cost': loaders_cost,
            'total_cost': total_cost,
            'discount_amount': discount_amount,
            'final_price': final_price
        })

    return render(request, 'progruz/price.html', {
        'truck_price': 80,
        'loader_price': 11
    })