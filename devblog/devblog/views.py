

from django.views import generic
from . import models

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = 'home.html'
    paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        blog_entries = models.Entry.objects.all()
        paginator = Paginator(blog_entries, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            entry_page = paginator.page(page)
        except PageNotAnInteger:
            entry_page = paginator.page(1)
        except EmptyPage:
            entry_page = paginator.page(paginator.num_pages)

        context['object_list'] = entry_page
        context['recent_entries'] = blog_entries
        return context

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        blog_entries = models.Entry.objects.all()
        
        context['recent_entries'] = blog_entries
        return context
