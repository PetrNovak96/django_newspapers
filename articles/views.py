from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .models import Article


class ArticleListView(LoginRequiredMixin,ListView):

    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    login_url = 'login'  # new

class ArticleDetailView(LoginRequiredMixin,DetailView):

    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'  # new

class ArticleUpdateView(LoginRequiredMixin,UpdateView):

    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'  # new

    def dispatch(self, request, *args, **kwargs):  # new (takovy interceptor)
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleDeleteView(LoginRequiredMixin,DeleteView):

    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'  # new

    def dispatch(self, request, *args, **kwargs):  # new (takovy interceptor)
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin,CreateView):

    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author',)
    login_url = 'login' # new

    def form_valid(self, form):
        form.instance.author = self.request.user # clanek vytvari prihlaseny uzivatel
        return super().form_valid(form)