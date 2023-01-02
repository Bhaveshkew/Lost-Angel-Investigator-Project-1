from django.contrib import admin
from calc.models import Person , RegisteredChild,User
# Register your models here.

admin.site.register(Person)
admin.site.register(RegisteredChild)
admin.site.register(User)