from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('Profile.urls')),
    path('report/', include('Reports.urls'))
]
