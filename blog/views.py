from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def category_list(request):
    categories = Category.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)

    return render(request, 'blog/category_list.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    return render(request, 'blog/category_detail.html', {'category': category}) # in this template, you will have access to category and posts under that category by (category.post_set).


def post_list_cultural_appropriation(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(category=1)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list_mmm(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(category=2)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list_rr(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(category=3)
    return render(request, 'blog/post_list.html', {'posts': posts})
#def post_list_cultural_appropriation(request):
#    posts = Post.objects.filter(category='Cultural Appropriation')
#    return render(request, 'blog/post_list_cultural_appropriation.html',{'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
        post.save()
        return redirect('post_detail', pk=post.pk)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
