from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    # Search query example - /movie/search/?query=the%20dark%20knight
    url(r'^search/$', views.search, name='search'),
]
