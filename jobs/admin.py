from django.contrib import admin

from .models import Job
from blog.models import Blog

admin.site.register(Job)
admin.site.register(Blog)
