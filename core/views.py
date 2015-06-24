from itertools import chain
from core.models import Page, News, Event
from django.shortcuts import render
from users.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def error404(request):
    return render(request, 'core/404.html')

def index(request):
    page_list = Page.objects.all()
    news_list = News.objects.all()
    event_list = Event.objects.all()
    result_list = sorted(chain(page_list, news_list, event_list),
                         key=lambda x: x.date_updated, reverse=True)
    context = {
        'profile': User.objects.get(id=request.user.id),
        'result_list': result_list,
    }
    return render(request, 'core/index.html', context)


def feed(request):
    page_list = Page.objects.all()
    news_list = News.objects.all()
    event_list = Event.objects.all()
    result_list = sorted(chain(page_list, news_list, event_list),
                         key=lambda x: x.date_updated, reverse=True)
    paginator = Paginator(result_list, 9)
    page = request.GET.get('page')
    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)
    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)
    context = {
        'result_list': result_list,
    }
    return render(request, 'core/feed.html', context)
