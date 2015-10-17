from django.conf.urls import url

from . import views

urlpatterns = [
    # Search query example - /movie/api/v1/search/?query=the%20dark%20knight
    # url(r'^api/v1/search/$', views.search, name='search'),
    # Show query example - /movie/api/v1/show/?query=imdbId
    url(r'^api/v1/show/$', views.show, name='show'),
    url(r'^api/v1/search/keyword', views.search, name='search')
]
