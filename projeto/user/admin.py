from django.contrib import admin
from .models import User 

#adicionando User no admin
admin.site.register(User)
# Register your models here.
