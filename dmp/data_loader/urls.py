from django.conf.urls import url

from data_loader.views import DataSourceListView, DataSourceCreateView, DataProviderListView, DataSourceDeleteView

urlpatterns = [
    url(r'^$', DataSourceListView.as_view(), name='datasource-list'),
    url(r'create/$', DataSourceCreateView.as_view(), name='datasource-create'),
    url(r'delete/(?P<pk>[0-9]+)/$', DataSourceDeleteView.as_view(), name='datasource-delete'),
    url(r'data-providers/$', DataProviderListView.as_view(), name='datasource-providers')
]