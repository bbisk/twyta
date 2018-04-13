from django import forms
from app.models import Tweet, Message


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Tweet
        exclude = ('author',)


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('already_read', 'from_user', 'to_user')