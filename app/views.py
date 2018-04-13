from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from app.forms import AddPostForm
from app.models import Tweet

TEMP_MAIN = 'main.html'

class MainPageView(ListView):
    template_name = TEMP_MAIN
    queryset = Tweet.objects.all()

class AddPostView(CreateView):
    form_class = AddPostForm
    template_name = TEMP_MAIN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Tweet.objects.all()
        return context