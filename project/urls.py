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
]
