import re

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import CreateView
from models import Post, Author, Comment


class IndexView(CreateView):
    template_name = 'blog/index.html'
    context_object_name = 'ps'

    def get(self, request, *args, **kwargs):
        ps = Post.objects.order_by('-pub_date')[:10]
        return render(request, 'blog/index.html', {'ps': ps, 'title': 'Blog Index'})

    def post(self, request, *args, **kwargs):
        a = get_object_or_404(Author, nickname='bearzk')
        title = request.POST['title'].strip()
        slug = re.sub('\s', '-', title.lower())
        p = a.post_set.create(title=title, slug=slug, content=request.POST['content'],
                              pub_date=timezone.now())
        p.save()
        return redirect('blog:index')

def detail(request, post_slug):
    p = get_object_or_404(Post, slug=post_slug)
    a = get_object_or_404(Author, pk=p.author_id)
    cs = Comment.objects.filter(post_id=p.id)
    return render(request, 'blog/detail.html', {'p': p, 'a': a, 'cs': cs})


def author(request, author_name):
    a = get_object_or_404(Author, nickname=author_name)
    return render(request, 'blog/author.html', {'a': a})


def add_comment(request, post_slug):
    p = get_object_or_404(Post, slug=post_slug)
    c = p.comment_set.create(content=request.POST['content'], pub_date=timezone.now())
    c.save()
    return redirect('blog:detail', post_slug=p.slug)


class CommentView(CreateView):
    template_name = 'blog/comment.html'
    context_object_name = 'cs'

    def post(self, request, *args, **kwargs):
        p = get_object_or_404(Post, post_id=request.POST['post_id'])
        a = get_object_or_404(Author, nickname='bearzk')
        content = request.POST['content'].strip()
        c = p.post_set.create(content=content, post_id=p.id, author_id=a.id)
        c.save()
        return redirect('detail', slug=p.slug)
