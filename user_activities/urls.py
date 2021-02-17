from django.contrib import admin
from django.urls import path
from activity_logger import views
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register(r'activity_loggers', views.UserDataView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
