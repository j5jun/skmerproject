from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('upload/', views.CreatePostView.as_view(), name='upload')
]
