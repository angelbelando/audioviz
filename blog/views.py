from django.views.generic.dates import DateDetailView
from django.views import generic
from .models import Post


class BlogNewListView(generic.ListView):
    model = Post
    context_object_name = "posts"
    template_name = 'blog/post_new_list.html'
    queryset = Post.objects.all().select_related()
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogDetailView(DateDetailView):
    model = Post
    context_object_name = "post"
    date_field = 'post_date'
    month_format = '%m'
    template_name = 'blog/post_new_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
