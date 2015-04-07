from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from studycollab import views
from django.contrib import admin

urlpatterns = patterns('',
   url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
   url(r'^register/$', views.register, name='register'),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^findGroup/$', views.findGroup, name = 'findGroup'),
   )
