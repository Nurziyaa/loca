from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
    url(r'^', include('mainApp.urls')),
    url(r'^webexample/', include('webexample.urls')),
]
