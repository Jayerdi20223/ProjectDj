from django.test import TestCase

from app.wsgi import *
from core.erp.models import Type, Employee

# Create your tests here.

# LISTAR

# query = Type.objects.all()
# print(query)

# INSERTAR

# t = Type()
# t.name = "Accionista"
# t.save()

# EDITAR

# t = Type.objects.get(pk=1)
# t.name = "Presidente"
# t.save()

# ELIMINAR

# t = Type.objects.get(pk=1)
# t.delete()

# obj = Type.objects.filter(name__icontains="terry")

obj = Employee.objects.filter()

for i in Type.objects.filter():
    print(i.name)
