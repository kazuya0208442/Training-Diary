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
       s_time = Training.objects.values_list('sleeping_hours', flat=True)
       s_time = [float(v) for v in s_time]    # DECIMAL prefix を外す方法
       context = super(Home, self).get_context_data(**kwargs)
       context.update({
           'training': Training.objects.all(),
           'week': Week.objects.all(),
           'staff': Staff.objects.all(),
           'test': test,
           's_time': s_time,
       })
       return context


class Target_detail(DetailView):
    template_name = 'app_target_detail.html'
    model = Target


class Card_detail(DetailView):
    template_name = 'app_card_detail.html'
    model = Training


class Week_detail(DetailView):
    template_name = 'app_week_detail.html'
    model = Week


class Staff_detail(DetailView):
    template_name = 'app_staff_detail.html'
    model = Staff


class TargetUpdate(UpdateView):
    template_name = 'app_target_update.html'
    model = Target
    fields = ('long_target', 'long_target_summary', 'long_target_date', 'middle_target', 'middle_target_summary', 'short_target', 'short_target_summary')
    # success_url = reverse_lazy('t_detail')      # 静的ページにしか使えない。
    def get_success_url(self):
        return reverse_lazy('t_detail', kwargs={'pk': self.kwargs['pk']})


class CardUpdate(UpdateView):
    template_name = 'app_card_update.html'
    model = Training
    fields = ('dairy_target', 'dairy_target_menu', 'dairy_target_summary', 'training_time', 'stability_time', 'stretch_time', 'body_temperature', 'body_weight', 'sleeping_hours')
    # success_url = reverse_lazy('t_detail')      # 静的ページにしか使えない。
    def get_success_url(self):
        return reverse_lazy('c_detail', kwargs={'pk': self.kwargs['pk']})