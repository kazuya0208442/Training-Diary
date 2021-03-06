from django.db.models import fields
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Staff, Target, Training, Week
from django.urls import reverse_lazy
from .change_link import change_link
from .day_computed import day_computed

# Create your views here.

class Home(ListView):
   template_name = 'app_home.html'
   context_object_name = 'target'
   model = Target
   
   def get_context_data(self, **kwargs):

       # [Decimal('11.16'), Decimal('7.63'), Decimal('8.53')] のような 'Decimal' prefix を取り除くために float() を用いて、小数値を取得。
       def _to_float(x_list):
           return [float(v) for v in x_list]
       
       # 大会の日程を取得
       target_date = Target.objects.values('long_target_date').get(pk=1)['long_target_date']
       # 大会まで残り何日なのかを計算
       time_delta = day_computed(target_date)

       # 運動時間を取得
       t_time = Training.objects.values_list('training_time', flat=True)
       # DECIMAL prefix を外す
       t_time_new = _to_float(t_time)

       # 体幹トレーニング時間を取得
       stability_time = Training.objects.values_list('stability_time', flat=True)
       # DECIMAL prefix を外す
       stability_time_new = _to_float(stability_time)

       # 睡眠時間を取得
       s_time = Training.objects.values_list('sleeping_hours', flat=True)
       # DECIMAL prefix を外す
       s_time_new = _to_float(s_time)    

       # 長期目標のYouTube Link を取得
       link = Target.objects.values('long_target_link').get(pk=1)['long_target_link']
       # YouTube の再生開始時間を取得
       link_start = Target.objects.values('long_target_link_start').get(pk=1)['long_target_link_start']
       # 長期目標のYouTube Link を改造(自動再生あり)
       link_long = change_link(link, auto=1, start=link_start)
       # 中期目標のYouTube Link を改造(自動再生なし)
       link_middle = change_link(Target.objects.values('middle_target_link').get(pk=1)['middle_target_link'], auto=0)
       # 短期目標のYouTube Link を改造(自動再生なし)
       link_short = change_link(Target.objects.values('short_target_link').get(pk=1)['short_target_link'], auto=0)

       # context を追加することで、HTMLの中から呼び出すことが可能
       context = super(Home, self).get_context_data(**kwargs)
       context.update({
           'training': Training.objects.all(),
           'week': Week.objects.all(),
           'staff': Staff.objects.all(),
           't_time_new': t_time_new,
           'stability_time_new': stability_time_new,
           's_time_new': s_time_new,
           'link_long': link_long,
           'link_middle': link_middle,
           'link_short': link_short,
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
    fields = ('dairy_target', 'dairy_target_menu', 'dairy_target_summary', 'training_time', 'stability_time', 'stretch_time', 'body_temperature', 'body_weight', 'sleeping_hours', 'date')
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

class Test(ListView):
   template_name = 'a.html'
   model = Target