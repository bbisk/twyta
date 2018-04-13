from django.contrib import admin

# Register your models here.
from app.models import Message
from .models import Tweet

admin.site.register(Tweet)
admin.site.register(Message)