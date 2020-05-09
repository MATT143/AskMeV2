from django.forms import ModelForm
from .models import Post

class PostQuestionForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','content','category']