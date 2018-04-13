from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.detail import DetailView
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

    def form_valid(self, form):
        post_form = form.save(commit=False)
        post_form.author = self.request.user
        post_form.save()
        return redirect('main')

class UserPostView(ListView):
    template_name = TEMP_MAIN

    def get_queryset(self):
        queryset = Tweet.objects.filter(author=self.request.user)
        return queryset


class PostDetailView(DetailView):
    template_name = 'post.html'
    queryset = Tweet.objects.all()