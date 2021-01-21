from django.contrib import admin

# Register your models here.
from .models import UsersAll,Worked,Material

admin.site.register(UsersAll)
admin.site.register(Worked)
admin.site.register(Material)