from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from .models import Photo


# Create your views here.
class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'


class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # if correct
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/'


class PhotoUpdate(UpdateView):
    model = Photo
    template_name_suffix = '_update'
    success_url = '/'


class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'
