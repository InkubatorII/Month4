from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm2, SearchForm
from django.db.models import Q

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
        return render(
            request, 'posts/post_list.html',
            context=context
        )

@login_required(login_url='/login/')
def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'posts/post_detail.html', context={'post': post})

@login_required(login_url='/login/')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        form.save()
        return redirect('/posts/')


