from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/?$', 'chat.views.home.home_handler', name='home'),
    url(r'^login/?$', 'chat.views.home.login_handler', name='login'),
    url(r'^logout/?$', 'chat.views.home.logout_handler', name='logout'),
    url(r'^api/message/?$', 'chitchat.api.message_get_handler'),
)
