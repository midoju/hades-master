from config.wsgi import *
from core.erp.models import *

# LISTAR

#print(Category.objects.all())

#for i in Category.objects.filter():
    print(i)

data = [ 'Leche y derivados', 'Carnes, pescado y huevos', 'Patatas, legumbres, frutos secos',
    'Verduras y Hortalizas','Frutas', 'Cereales y derivados', 'azucar y dulces', 'Grasas, aceite y mantequilla' 
]

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))