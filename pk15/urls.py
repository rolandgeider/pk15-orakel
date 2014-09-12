from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # Core (login, common templates, etc.)
    url(r'^', include('core.urls', namespace='core', app_name='core')),

    # Oracle app
    url(r'^orakel/', include('oracle.urls', namespace='oracle', app_name='oracle')),
)
