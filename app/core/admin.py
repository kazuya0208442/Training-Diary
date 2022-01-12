from django.contrib import admin
from core.models import Sample
from .models import Training, TodoModel     #エラー出たから分けたけど、関係ないかも

# Register your models here.
admin.site.register(Sample)
# admin.site.register(TodoModel)
admin.site.register(TodoModel)
admin.site.register(Training)