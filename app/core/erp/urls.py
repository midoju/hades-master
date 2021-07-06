from django.urls import path

#from core.erp.views import myfirstview, mysecondview
from core.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list1', category_list),
    path('category/list', CategoryListView.as_view(), name='category_list'),
    path('category/add', CategoryCreateView.as_view(), name='category_add'),
    path('category/edit/<int:pk>', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),

    #path('uno/', myfirstview, name='vista1'),
    #path('dos/', mysecondview, name='vista2')
]
