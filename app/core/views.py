from django.db.models import fields
# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Staff, Target, TodoModel, Training, Week
from django.urls import reverse_lazy



# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')



class Home(ListView):
   template_name = 'app_home.html'
   context_object_name = 'target'
   model = Target
   

   def get_context_data(self, **kwargs):
       test = Target.objects.values_list('long_target', flat=True)
       context = super(Home, self).get_context_data(**kwargs)
       context.update({
           'training': Training.objects.all(),
           'week': Week.objects.all(),
           'staff': Staff.objects.all(),
           'test': test,
       })
       return context


class Target_detail(DetailView):
    template_name = 'app_target_detail.html'
    model = Target


class Card_detail(DetailView):
    template_name = 'app_card_detail.html'
    model = Training