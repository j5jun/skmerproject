from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView  # new
from django.shortcuts import render, redirect

from .forms import uploadForm, resultsForm
from .models import upload, results


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
    model = results
    form_class = resultsForm
    template_name = 'results.html'
    success_url = reverse_lazy('home')

    def get(self, request):
        #form_class = self.get_form_class()
        form = resultsForm()
        f = open('test.csv', 'r')
        i = 0
        tmp = {}
        for line in f:
            line = line.split(",")
            i +=1
            if i == 1:
                tmp["genome_size"] = line[1]
            elif i == 2:
                tmp["repeat"] = line[1]
            elif i ==3:
                tmp["tax_ID"] = line[1]
            elif i == 4:
                tmp["dist"] = line[1]
            else:
                break
        f.close()

        form = resultsForm(tmp)
        #if form.is_valid():
            #return self.form_valid(form)
        #else:
        #    return self.form_invalid(form)
        return render(request, self.template_name, {'form': form})


def import_db():
    f = open('test.csv', 'r')
    for line in f:
        tmp = resultsForm()
        tmp.genome_size = line[0]
        tmp.repeat = line[1]
        tmp.tax_ID = line[2]
        tmp.dist = line[3]
    f.close()
    return tmp


# def model_form_upload(request):
#     if request.method == 'GET':
#         form = resultsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             print(form.upload.name)
#             return redirect('../templates/results.html')
#     else:
#         form = uploadForm()
#
#     return render(request, '../templates/upload.html', {
#             'form': form})

