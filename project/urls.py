from django.conf.urls import include, url
from django.contrib import admin

from blocks import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$', views.ListBlocksView.as_view(), name='blocks-list'),
    url('^blocks/new$', views.CreateBlockView.as_view(), name='blocks-new'),
    url('^blocks/(?P<pk>\d+)/$', views.EditBuildingsView.as_view(),
        name='buildings-edit'),
    url('^blocks/dynamic/(?P<pk>\d+)/$', views.EditBuildingsDynamicView.as_view(),
        name='buildings-edit-dynamic'),
    url('^blocks/dynamic-tabs/(?P<pk>\d+)/$', views.EditBuildingsDynamicTabsView.as_view(),
        name='buildings-edit-dynamic-tabs'),
    url('^blocks/dynamic-tabs-nested/(?P<pk>\d+)/$', views.EditBuildingsDynamicTabsNestedView.as_view(),
        name='buildings-edit-dynamic-tabs-nested'),
]
