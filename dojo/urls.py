# dojo/urls.py
from django.conf.urls import url
from . import views
from . import views_cbv
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^sum/(?P<x>\d+)/$', views.mysum),
    #url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    #url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),

    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^list4/$', views.excel_download),

    url(r'^cbv/list1/$', views_cbv.PostListView1),
    #url(r'^cbv/list2/$', views_cbv.PostListView2),
    #url(r'^cbv/list3/$', views_cbv.PostListView3),
    #url(r'^cbv/list4/$', views_cbv.Excel_download),
]