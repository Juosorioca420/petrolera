from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Factura, Acta, Campo

# group = Group.objects.create(name='accountant ')
# group = Group.objects.create(name='logistics')
# group = Group.objects.create(name='manager')

# Register your models here.
admin.site.register(Factura)
admin.site.register(Acta)
admin.site.register(Campo)
