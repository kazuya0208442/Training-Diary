# Generated by Django 3.2.11 on 2022-01-13 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211004_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='タイトル', max_length=100)),
                ('staff', models.TextField(help_text='スタッフから')),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_target', models.CharField(help_text='長期目標', max_length=100)),
                ('long_target_summary', models.TextField(help_text='長期目標の詳細について')),
                ('long_target_date', models.DateField(default=datetime.datetime.now, help_text='長期目標の期日')),
                ('middle_target', models.CharField(help_text='中期目標', max_length=100)),
                ('middle_target_summary', models.TextField(help_text='中期目標の詳細について')),
                ('short_target', models.CharField(help_text='短期目標', max_length=100)),
                ('short_target_summary', models.TextField(help_text='短期目標の詳細について')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dairy_target', models.CharField(help_text='今日のタイトル', max_length=100)),
                ('dairy_target_menu', models.TextField(help_text='トレーニングメニュー')),
                ('dairy_target_summary', models.TextField(help_text='意識したこと・達成したこと')),
                ('training_time', models.DecimalField(decimal_places=1, default=0, help_text='運動の合計時間', max_digits=4)),
                ('stability_time', models.DecimalField(decimal_places=1, default=0, help_text='体幹トレーニングの合計時間', max_digits=4)),
                ('stretch_time', models.DecimalField(decimal_places=1, default=0, help_text='ストレッチの合計時間', max_digits=4)),
                ('body_temperature', models.DecimalField(decimal_places=1, default=0, help_text='体温', max_digits=4)),
                ('body_weight', models.DecimalField(decimal_places=1, default=0, help_text='体重', max_digits=4)),
                ('sleeping_hours', models.DecimalField(decimal_places=1, default=0, help_text='睡眠時間', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='今週のタイトル', max_length=100)),
                ('summary', models.TextField(help_text='今週の振り返り')),
            ],
        ),
    ]