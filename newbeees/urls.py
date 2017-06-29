from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'newbeees.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'poster.views.index'),
    url(r'^ABOUT/', 'poster.views.about'),
    url(r'^(?P<pk>\d+)/$', 'poster.views.honey_list'),
    url(r'^(?P<honeycomb>\w+)/$', 'poster.views.honeycomb_detail'),
    url(r'^new/$', 'poster.views.new_honey'),
]
