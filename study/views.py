from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from . import models
from . import forms


# Create your views here.


@login_required
def list(request):
    """一覧画面

    Returns:
        object:
    """
    posts = models.Post.objects.order_by('-create_at')
    data = {'posts': posts}
    return render(request, 'list.html', data)


@login_required
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
            # formからmodelへデータを渡す
            post = models.Post()
            post.title = form.data['title']
            post.content = form.data['content']
            # データの保存
            post.save()
            return redirect('study:list')
        else:
            return render(request, 'new.html', {'form': form})
    else:
        form = forms.PostForm()
        return render(request, 'new.html', {'form': form})


@login_required
def detail(request, post_id):
    """ 詳細画面への遷移

    Returns:
        object:
    """
    if request.method == "GET":
        # データが存在しない場合404エラーを追加
        # post = models.Post.objects.get(pk=post_id)
        post = get_object_or_404(models.Post, pk=post_id)
        data = {'post': post}
        return render(request, 'detail.html', data)
    else:
        return render(request, 'errors/405.html', status=405)


@login_required
def edit(request, post_id):
    """編集画面へ遷移

    Returns:
        object:
    """
    # 編集するためのデータをDBから持ってくる
    post = models.Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        # validation check
        if form.is_valid():
            post.title = form.data['title']
            post.content = form.data['content']
            post.save()
            return redirect('study:list')
        else:
            return render(request, 'edit.html', {'form': form})
    else:
        form = forms.PostForm(instance=post)
        return render(request, 'edit.html', {'form': form})
