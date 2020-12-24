from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models
from . import forms


# Create your views here.


def list(request):
    posts = models.Post.objects.all().order_by('-create_at')
    data = {'posts': posts}
    return render(request, 'list.html', data)


def new(request):
    """新規作成

    Args:
        request:

    Returns:
        POST:
            return (redirect): 投稿に成功したら記事一覧に遷移する
            return (render): validationに引っかかったら戻る
        GET:
            return (render): 新規投稿画面へ遷移


    """
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = models.Post()
            post.title = form.data['title']
            post.content = form.data['content']
            post.save()
            return redirect(reverse_lazy('list'))
        else:
            return render(request, 'new.html', {'form': form})
    else:
        form = forms.PostForm()
        return render(request, 'new.html', {'form': form})


def detail(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    data = {'post': post}
    return render(request, 'detail.html', data)


def edit(request, post_id):
    print('post_id:', post_id)
    post = models.Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post.title = form.data['title']
            post.content = form.data['content']
            post.save()
            return redirect(reverse_lazy('list'))
        else:
            return render(request, 'edit.html', {'form': form})
    else:
        form = forms.PostForm(instance=post)
        return render(request, 'edit.html', {'form': form})

