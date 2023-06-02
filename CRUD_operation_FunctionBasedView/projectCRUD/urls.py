from django.contrib import admin
from django.urls import path
from enroll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name="addshow"),
    path('delete/<int:id>/', views.delete_data, name="deleteOne"),
    path('updt/<int:id>/', views.update_data, name="update"),
]
