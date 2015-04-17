from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from studycollab import views
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
   url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
   url(r'^register/$', views.register, name='register'),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^browse/$', views.findInformation, name = 'findInformation'),
   url(r'^addGroup/$', views.addGroup, name = 'addGroup'),
   url(r'^addDocument/$', views.addDocument, name = 'addDocument'),
   url(r'^displayGroup/(?P<groupvalue>[a-zA-Z0-9]+)$', views.displayGroup, name = 'displayGroup'),
   url(r'^login/$', views.login, name = 'login'),
   url(r'^help/$', views.displayHelp, name = 'help'),
   url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': 'index'}),
   ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
