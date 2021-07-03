from django.urls import path

#from core.erp.views import myfirstview, mysecondview
from core.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list', category_list),
    path('category/list1', CategoryListView.as_view())
    #path('uno/', myfirstview, name='vista1'),
    #path('dos/', mysecondview, name='vista2')
]
