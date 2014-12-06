import re

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from models import Post, Author


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'ps'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]

    def add(self, request):
        a = get_object_or_404(Author, nickname='bearzk')
        title = request.POST['title'].strip()
        slug = re.sub('\s', '-', title.lower())
        p = a.post_set.create(title=title, slug=slug, content=request.POST['content'],
                              pub_date=timezone.now())
        p.save()
        return redirect('blog:index')


def detail(request, post_id):
    p = get_object_or_404(Post, id=post_id)
    a = get_object_or_404(Author, pk=p.author_id)
    return render(request, 'blog/detail.html', {'p': p, 'a': a})


def author(request, author_name):
    a = get_object_or_404(Author, nickname=author_name)
    return render(request, 'blog/author.html', {'a': a})

