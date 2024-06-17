from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView



def order_home(request):
    order = Articles.objects.order_by('-date')
    return render(request, 'order/order_home.html', {'order': order})


class OrderDetailView(DetailView):
    model = Articles
    template_name = 'order/details_view.html'
    context_object_name = 'article'


class OrderUpdateView(UpdateView):
    model = Articles
    template_name = 'order/create.html'

    form_class = ArticlesForm


class OrderDeleteView(DeleteView):
    model = Articles
    success_url = '/order/'
    template_name = 'order/order-delete.html'


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'order/create.html', data)
