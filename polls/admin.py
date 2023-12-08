from django.contrib import admin
from .models import Choice, Question

# Register your models here to be displayed on the admin site
admin.site.register(Choice)
admin.site.register(Question)
