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

    dairy_target = models.CharField(max_length=100, help_text='今日のタイトル')
    dairy_target_menu = models.TextField(help_text='トレーニングメニュー')
    dairy_target_summary = models.TextField(help_text='意識したこと・達成したこと')
    
    training_time = models.DecimalField(default=0, help_text='運動の合計時間(hour)', decimal_places=1, max_digits=4)
    stability_time = models.IntegerField(default=0, help_text='体幹トレーニングの合計時間(min)')
    stretch_time = models.IntegerField(default=0, help_text='ストレッチの合計時間(min)')
    body_temperature = models.DecimalField(default=0, help_text='体温', decimal_places=1, max_digits=4)
    body_weight = models.DecimalField(default=0, help_text='体重', decimal_places=1, max_digits=4)
    sleeping_hours = models.DecimalField(default=0, help_text='睡眠時間(hour)', decimal_places=1, max_digits=4)

    date = models.DateField(default=timezone.datetime.now, help_text='日付')

    def __str__(self):
        return self.dairy_target


class Target(models.Model):
    long_target = models.CharField(max_length=100, help_text='長期目標')
    long_target_summary = models.TextField(help_text='長期目標の詳細について')
    long_target_date = models.DateField(default=timezone.datetime.now, help_text='長期目標の期日')
    long_target_link = models.TextField(help_text='YouTube の埋め込みリンク', blank=True, null=True)
    long_target_link_start = models.IntegerField(default=0, help_text='YouTube の再生開始時間', blank=True, null=True)

    middle_target = models.CharField(max_length=100, help_text='中期目標')
    middle_target_summary = models.TextField(help_text='中期目標の詳細について')
    middle_target_link = models.TextField(help_text='YouTube の埋め込みリンク', blank=True, null=True)
    middle_target_link_start = models.IntegerField(default=0, help_text='YouTube の再生開始時間', blank=True, null=True)


    short_target = models.CharField(max_length=100, help_text='短期目標')
    short_target_summary = models.TextField(help_text='短期目標の詳細について')
    short_target_link = models.TextField(help_text='YouTube の埋め込みリンク', blank=True, null=True)
    short_target_link_start = models.IntegerField(default=0, help_text='YouTube の再生開始時間', blank=True, null=True)


    def __str__(self):
        return self.long_target


class Week(models.Model):
    title = models.CharField(max_length=100, help_text='今週のタイトル')
    summary = models.TextField(help_text='今週の振り返り')

    def __str__(self):
        return self.title


class Staff(models.Model):
    title = models.CharField(max_length=100, help_text='タイトル')
    staff = models.TextField(help_text='スタッフから')

    def __str__(self):
        return self.title
