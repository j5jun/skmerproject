from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView  # new
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import uploadForm  # new
from .models import upload


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CreatePostView(CreateView):  # new
    model = upload
    form_class = uploadForm
    template_name = 'upload.html'
    success_url = reverse_lazy('results')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file_name = request.FILES['upload']
        if form.is_valid():
            print(file_name)  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ResultView(CreateView):  # new
    model = upload
    form_class = uploadForm
    template_name = 'results.html'
    success_url = reverse_lazy('home')


# def model_form_upload(request):
#     if request.method == 'POST':
#         for filename, file in request.FILES.iteritems():
#             name = request.FILES[filename].name
#         return HttpResponse(name)


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = uploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             print(form.upload.name)
#             return redirect('../templates/results.html')
#     else:
#         form = uploadForm()
#
#     return render(request, '../templates/upload.html', {
#             'form': form})
