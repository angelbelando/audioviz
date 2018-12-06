from django.urls import re_path

from .views import BlogDetailView, BlogNewListView

urlpatterns = [
                re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-_\w]+)/$',
                    BlogDetailView.as_view(),
                    name='blog_detail',
                    ),
                 re_path(r'^$', BlogNewListView.as_view(), name='blog_index'),
            ]
