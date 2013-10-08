from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# http://django-tastypie.readthedocs.org/en/latest/index.html

from tastypie.api import Api
from {{ project_name }}.api_v1 import *

api_v1 = Api(api_name='v1')
#api_v1.register(SessionResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(api_v1.urls)),
)

