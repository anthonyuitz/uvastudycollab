from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from studycollab import views

urlpatterns = patterns('',
   url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
   url(r'^register/$', views.register, name='register'),
   )
