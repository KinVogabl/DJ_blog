from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger
from .forms import CommentForm
from taggit.models import Tag

def posts_views(request, tag_slug=None):

    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = posts.filter(tags__in=[tag])
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    return render(request, 'posts.html', {'posts': posts,
                                          'page': page,
                                          'tag':tag })


def post_views(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment.filter(active=True)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return render(request, 'post.html', {'post': post,
                                         'comments': comments,
                                         'form': form})
