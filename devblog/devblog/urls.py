from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),

    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name='entry_detail'),

)
