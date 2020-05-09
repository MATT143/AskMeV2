from django.urls import path
from . import views
from .views import CreatePostView,home,GetSolutionView,PostDetailsView

urlpatterns = [
    path('',home,name='quest-home'),
    path('post/new/',CreatePostView.as_view(), name='post-create'),
    path('post/<uuid:pk>/',PostDetailsView.as_view(), name='post-detail'),
    path('post/<int:pk>/',PostDetailsView.as_view(), name='post-detail'),
    path('post/solution/sync',GetSolutionView.as_view(), name='solution-sync')
]
