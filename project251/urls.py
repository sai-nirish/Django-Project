from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project251.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('signin.urls')),
    url(r'^signin/', include('signin.urls')),
    url(r'^main/', include('main.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/accounts/password_reset/mailed/'},name="password_reset"),
    url(r'^accounts/password_reset/mailed/$','django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password_reset/(?P<uid36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$','django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/accounts/password_reset/complete/'}),
    url(r'^accounts/password_reset/complete/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change',{'post_change_redirect' : '/accounts/password_change/done/'}, name="password_change"),
    url(r'^accounts/password_change/done/$', 'django.contrib.auth.views.password_change_done'),
)
