from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Article
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.all()
    print(articles)
    return render(request, 'home.html', {'articles': articles})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"{reverse('article_list')}?success=true")
    else:
        form = ArticleForm()
    return render(request, 'Article/article_create_form.html', {'form': form})

@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"{reverse('article_list')}?success=true")
    else:
        form = ArticleForm(instance=article)
    return render(request, 'Article/article_update_form.html', {'form': form, 'article': article})

@login_required
def article_update_form(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(instance=article)
    return render(request, 'Article/article_update_form.html', {'form': form, 'article': article})

@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return HttpResponseRedirect(f"{reverse('article_list')}?success=true")
    return render(request, 'Article/article_confirm_delete.html', {'article': article})

