# coding: utf-8
from itertools import chain
from core.models import Page
from users.models import User
from water.models import News, Event
from django.shortcuts import render, get_object_or_404


def error404(request):
    return render(request, 'core/404.html')


def index(request):
    news_list = News.objects.all()
    event_list = Event.objects.all()
    result_list = sorted(chain(news_list, event_list),
                         key=lambda x: x.date_updated, reverse=True)
    context = {
        'profile': User.objects.get(id=request.user.id),
        'result_list': result_list,
        'noob': User.objects.order_by('-score_die')[:3],
        'guru': User.objects.order_by('-score_kill')[:3],
    }
    return render(request, 'core/index.html', context)


def page(request, page):
    article = get_object_or_404(Page, page=page)
    context = {
        'page': Page.objects.get(page=article.page),
    }
    return render(request, 'core/static.html', context)

    # TODO Ну тут видишь надо сделать так чттб после
    # окончания регистрации никто не мог подать заявку до следующей
