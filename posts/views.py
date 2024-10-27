from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from posts.models import Post, Comment
from posts.forms import SearchForm, CommentForm, PostForm
from django.db.models import Q
from django.views.generic import ListView, DetailView
'''
posts = [post1, post2, post3, post4, post5, post6 , post7 , post8 , post9 , post10]
limit = 2
page = 1

start = (page-1) * limit
end = page * limit
'''

def test_view(request):
    return HttpResponse('Hello world')

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'base.html')

@login_required(login_url='/login/')
def post_list_view(request):
    limit = 3
    if request.method == 'GET':
        search = request.GET.get('search', None)
        tag = request.GET.getlist('tag', None)
        ordering = request.GET.get('ordering', None)
        page = int(request.GET.get('page', 1))

        posts = Post.objects.all()

        if search:
            posts = posts.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        if tag:
            posts = posts.filter(tags__id__in=tag)
        if ordering:
            print(ordering)
            posts = posts.order_by(ordering)

        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]

        form = SearchForm()
        context={'posts': posts, 'form': form, 'max_pages': range(1, max_pages+1)}
        return render(request, 'posts/post_list.html', context=context)

class PostListView2(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


@login_required(login_url='/login/')
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = CommentForm()
        comments = post.comments.all()
        return render(request,
                      'posts/post_detail.html',
                      context={'post': post, 'form': form, 'comments': comments},
        )

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                'posts/post_detail.html',
                context={'post': post, 'form': form, 'comments': comments},
            )
        Comment.objects.create(text=form.cleaned_data['text'], post=post)
        return redirect(f'/posts/{post.id}')

class PostDetailView2(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'posts'
    lookup_url_kwarg = 'post_id'

@login_required(login_url='/login/')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm ()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        tags = form.cleaned_data.pop('tags')
        post = Post.objects.create(author=request.user, **form.cleaned_data)
        post.tags.set(tags)
        post.save()
        return redirect('/posts/')

@login_required(login_url='/login/')
def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = PostForm2(instance=post)
        return render(request, 'posts/post_update.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        form.save()
        return redirect('/profile/')






