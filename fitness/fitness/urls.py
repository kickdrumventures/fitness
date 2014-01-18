from django.conf.urls import patterns, include, url
from fitness import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fitness.views.home', name='home'),
    # url(r'^fitness/', include('fitness.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^workouts/', include('workouts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),


    #User authentication
    url(r'^accounts/login/$', 'fitness.views.login'),
    url(r'^accounts/auth/$', 'fitness.views.auth_view'),
    url(r'^accounts/logout/$', 'fitness.views.logout'),
    url(r'^accounts/loggedin/$', 'fitness.views.loggedin'),
    url(r'^accounts/invalid/$', 'fitness.views.invalid_login'),
    url(r'^accounts/register/$', 'fitness.views.register_user'),
    url(r'^accounts/register_success/$', 'fitness.views.register_success'),

)
