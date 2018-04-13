"""twyta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from app.views import MainPageView, AddPostView, UserPostView, PostDetailView, UserMessageView, SendMessageView, \
    UserProfileView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^add/$', AddPostView.as_view(), name='add_post'),
    url(r'^me/$', UserPostView.as_view(), name="user_posts"),
    url(r'^user/(?P<pk>(\d)+)/$', UserProfileView.as_view(), name="profile"),
    url(r'^messages/$', UserMessageView.as_view(), name="user_messages"),
    url(r'^messages/send/$', SendMessageView.as_view(), name="send_message"),
    url(r'^post/(?P<pk>(\d)+)/$', PostDetailView.as_view(), name="post_details"),

]
