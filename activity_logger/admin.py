from django.contrib import admin
from .models import UserData
from .models import ActivityData


admin.site.register(UserData)
admin.site.register(ActivityData)
