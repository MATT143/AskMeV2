from django.urls import path
from . import views
from .views import CreatePostView,home,GetSolutionView,PostDetailsView,PostDeleteView

urlpatterns = [
    path('',home,name='quest-home'),
    path('post/new/',CreatePostView.as_view(), name='post-create'),
    path('post/<uuid:pk>/',PostDetailsView.as_view(), name='post-detail'),
    path('post/<int:pk>/',PostDetailsView.as_view(), name='post-detail'),
    path('post/<uuid:pk>/delete/',PostDeleteView.as_view(), name='post-delete' ),
    path('post/solution/sync',GetSolutionView.as_view(), name='solution-sync')
]
