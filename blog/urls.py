from django.urls import re_path

from .views import BlogDetailView, BlogListView, LatestEntriesFeed, BlogNewListView

urlpatterns = [
                re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-_\w]+)/$',
                    BlogDetailView.as_view(),
                    name='blog_detail',
                    ),
                re_path(r'^archive/$',
                    BlogListView.as_view(
                        template_name="blog/post_archive.html",
                        page_template="blog/post_archive_page.html"),
                        name="blog_archive"),
                re_path(r'^latest/feed/$', LatestEntriesFeed()),
                # re_path(r'^$', BlogListView.as_view(), name='blog_index'),
                 re_path(r'^$', BlogNewListView.as_view(), name='blog_index'),
            ]
