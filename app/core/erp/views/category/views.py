from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView


from core.erp.models import Category

def category_list(request):
    data={
        'title' : ' Listado de Categorias',
        'categorias' : Category.objects.all()
    }

    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name' : 'William' }
        return JsonResponse(data)

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['entity'] = 'Categorias'
        return context

