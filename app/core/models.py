from django.db import models
from django.utils import timezone

# Create your models here.
class Sample(models.Model):
    attachment = models.FileField()

CHOICE = (('danger', 'high'), ('warning', 'normal'), ('primary', 'low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = CHOICE
        )
    duedate = models.DateField()

    def __str__(self):
        return self.title


class Training(models.Model):
    long_target = models.CharField(max_length=100, help_text='長期目標')
    long_target_summary = models.TextField(help_text='長期目標の詳細について')
    long_target_date = models.DateField(default=timezone.datetime.now, help_text='長期目標の期日')

    middle_target = models.CharField(max_length=100, help_text='中期目標')
    middle_target_summary = models.TextField(help_text='中期目標の詳細について')

    short_target = models.CharField(max_length=100, help_text='短期目標')
    short_target_summary = models.TextField(help_text='短期目標の詳細について')

    dairy_target = models.CharField(max_length=100, help_text='今日のタイトル')
    dairy_target_menu = models.TextField(help_text='トレーニングメニュー')
    dairy_target_summary = models.TextField(help_text='意識したこと・達成したこと')
    
    training_time = models.IntegerField(default=0, help_text='運動の合計時間')
    stability_time = models.IntegerField(default=0, help_text='体幹トレーニングの合計時間')
    stretch_time = models.IntegerField(default=0, help_text='ストレッチの合計時間')
    body_temperature = models.IntegerField(default=0, help_text='体温')
    body_weight = models.IntegerField(default=0, help_text='体重')
    sleeping_hours = models.IntegerField(default=0, help_text='睡眠時間')

    week_summary = models.TextField(help_text='今週の振り返り')
    staff = models.TextField(help_text='スタッフから')

    def __str__(self):
        return self.long_target