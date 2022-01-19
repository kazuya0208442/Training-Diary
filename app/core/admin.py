from django.contrib import admin
from core.models import Sample
from .models import Training, Target, Week, Staff     #エラー出たから分けたけど、関係ないかも

# Register your models here.
admin.site.register(Sample)
admin.site.register(Training)
admin.site.register(Target)
admin.site.register(Week)
admin.site.register(Staff)