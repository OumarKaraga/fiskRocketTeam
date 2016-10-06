from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/$', views.showMain, name='showMain'),
    url(r'^nasa_reports/$', views.showReports, name='showReports'),
    url(r'^outreach/$', views.showOutreach, name='showOutreach'),
    url(r'^$', views.showHome, name='showHome'),
    url(r'^physics_tutorial/$', views.showNews, name='showNews'),
]