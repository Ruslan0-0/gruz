from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView



def order_home(request):
    order = Article.objects.order_by('-publish_date')
    return render(request, 'order/order_home.html', {'order': order})


class OrderDetailView(DetailView):
    model = Article
    template_name = 'order/details_view.html'
    context_object_name = 'article'


class OrderUpdateView(UpdateView):
    model = Article
    template_name = 'order/create.html'

    form_class = ArticleForm


class OrderDeleteView(DeleteView):
    model = Article
    success_url = '/order/'
    template_name = 'order/order-delete.html'


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = 'Форма была неверной'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'order/create.html', data)


def index(request):

    num_authors=Article.objects.count()

    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    return render(
        request,
        'index.html',
        context={'num_orders': num_orders, 'num_visits': num_visits}
    )