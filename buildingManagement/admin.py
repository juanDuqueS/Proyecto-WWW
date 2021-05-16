from buildingManagement.models import Build, Client, Employee
from django.contrib import admin
from buildingManagement import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Build)