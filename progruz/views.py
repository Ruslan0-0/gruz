from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'progruz/index.html', data)


def about(request):
    return render(request, 'progruz/about.html')

def contacts(request):
    return render(request, 'progruz/contacts.html')
