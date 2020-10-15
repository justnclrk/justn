from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from taggit.models import Tag
from django.shortcuts import redirect

from .forms import PostForm
from .models import Post


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.order_by('name')
        return context


class PostListView(TagMixin, ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(active=True).order_by('-date_posted')


class PostDetailView(TagMixin, DetailView):
    model = Post
    queryset = Post.objects.filter(active=True)


class PostCreateView(TagMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(TagMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'content', 'tags', 'active']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class TagIndexView(TagMixin, ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(active=True).filter(tags__slug=self.kwargs.get('slug')).order_by('-date_posted')
