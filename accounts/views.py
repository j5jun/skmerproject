from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView # new

from .forms import uploadForm # new
from .models import upload

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CreatePostView(CreateView): # new
    model = upload
    form_class = uploadForm
    template_name = 'upload.html'
    success_url = reverse_lazy('results')


class ResultView(CreateView):  # new
    model = upload
    form_class = uploadForm
    template_name = 'results.html'
    success_url = reverse_lazy('home')
