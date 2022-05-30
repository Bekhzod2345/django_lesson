from django.contrib import admin

# Register your models here.
from .models import Mashina


class MashinaModel(admin.ModelAdmin):
    list_display = ['id','nomi', 'rangi','yili']
    list_filter = ['yili','rangi' ]

admin.site.register(Mashina, MashinaModel)