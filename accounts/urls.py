from django.urls import path

from . import views
from .views import CreatePostView


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('upload/', CreatePostView.as_view(), name='add_post')
]
