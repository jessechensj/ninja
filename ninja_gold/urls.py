from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.ninja_gold.urls')),
    url(r'^ninja_gold/', include('apps.ninja_gold.urls'))
]
