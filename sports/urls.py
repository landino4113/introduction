from django.conf.urls import url
from . import views


urlpatterns = [
    # /sports/
    url(r'^$', views.index, name='index'),

    # /sports/712/
    # url(r'^(?P<team_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(\d)/$', views.detail, name='detail'),
]