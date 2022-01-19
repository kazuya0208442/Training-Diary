from django.db.models import fields
# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Staff, Target, TodoModel, Training, Week
from django.urls import reverse_lazy
from .change_link import change_link
from .day_computed import day_computed



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

       def _to_float(x_list):
           return [float(v) for v in x_list]
       
       target_date = Target.objects.values('long_target_date').get(pk=1)['long_target_date']
       time_delta = day_computed(target_date)

       t_time = Training.objects.values_list('training_time', flat=True)
       t_time_new = _to_float(t_time)
       stability_time = Training.objects.values_list('stability_time', flat=True)
       stability_time_new = _to_float(stability_time)
       s_time = Training.objects.values_list('sleeping_hours', flat=True)
       s_time_new = _to_float(s_time)    # DECIMAL prefix を外す方法

       link = Target.objects.values('long_target_link').get(pk=1)['long_target_link']
       link_start = Target.objects.values('long_target_link_start').get(pk=1)['long_target_link_start']
       new_link = change_link(link, link_start)

       context = super(Home, self).get_context_data(**kwargs)
       context.update({
           'training': Training.objects.all(),
           'week': Week.objects.all(),
           'staff': Staff.objects.all(),
           't_time_new': t_time_new,
           'stability_time_new': stability_time_new,
           's_time_new': s_time_new,
           'link_new_long': new_link,
           'time_delta': time_delta,
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
    fields = ('long_target', 'long_target_summary', 'long_target_date', 'long_target_link', 'long_target_link_start', 'middle_target', 'middle_target_summary', 'middle_target_link', 'short_target', 'short_target_summary', 'short_target_link')
    success_url = reverse_lazy('home')      # 静的ページにしか使えない。
    # def get_success_url(self):
    #     return reverse_lazy('t_detail', kwargs={'pk': self.kwargs['pk']})


class CardUpdate(UpdateView):
    template_name = 'app_card_update.html'
    model = Training
    fields = ('dairy_target', 'dairy_target_menu', 'dairy_target_summary', 'training_time', 'stability_time', 'stretch_time', 'body_temperature', 'body_weight', 'sleeping_hours')
    # success_url = reverse_lazy('t_detail')      # 静的ページにしか使えない。
    def get_success_url(self):
        return reverse_lazy('c_detail', kwargs={'pk': self.kwargs['pk']})


class StaffUpdate(UpdateView):
    template_name = 'app_staff_update.html'
    model = Staff
    fields = ('title', 'staff')
    success_url = reverse_lazy('home')      # 静的ページにしか使えない。


class WeekUpdate(UpdateView):
    template_name = 'app_week_update.html'
    model = Week
    fields = ('title', 'summary')
    success_url = reverse_lazy('home')      # 静的ページにしか使えない。