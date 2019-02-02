from django.conf.urls import url
from basic_templates_app import views


app_name = 'basic_templates_app'

urlpatterns = [
    url(r'^relative_url_templates/$', views.relative_url_templates, name='relative_url_templates'),
    url(r'^other/$', views.other, name='other'),
]
