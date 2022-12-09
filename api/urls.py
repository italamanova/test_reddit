from django.urls import path
from .views import LinkApiView, upvote, downvote, LinkDetailApiView

urlpatterns = [
    path('links', LinkApiView.as_view()),
    path('links/<int:pk>', LinkDetailApiView.as_view()),
    path('links/<int:pk>/upvote', upvote, name='upvote'),
    path('links/<int:pk>/downvote', downvote, name='downvote'),
]
