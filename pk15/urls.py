from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # Core (login, common templates, etc.)
    url(r'^', include('core.urls', namespace='core', app_name='core')),
    #url(r'^$', include('core.urls', namespace='core', app_name='core')),

    # Oracle app
    #url(r'^orakel/', include('orakel.urls', namespace='orakel', app_name='orakel')),
)
