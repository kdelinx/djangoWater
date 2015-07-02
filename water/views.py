# coding: utf-8
from users.models import User
from water.models import Event, News, Gallery, Videos

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from itertools import chain


def feed(request):
    news_list = News.objects.all()
    event_list = Event.objects.all()
    result_list = sorted(chain(news_list, event_list),
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


@login_required
def likes_gallery(request, id):
    user = get_object_or_404(User, id=request.user.id)
    gallery = get_object_or_404(Gallery, id=id)
    if user in gallery.objects.all():
        gallery.likes.remove(user)
    else:
        gallery.likes.add(user)
    return HttpResponseRedirect(
        reverse('water:gallery', args=(gallery.id,))
    )


@login_required
def likes_videos(request, id):
    user = get_object_or_404(User, id=request.user.id)
    video = get_object_or_404(Videos, id=id)
    if user in video.objects.all():
        video.likes.remove(user)
    else:
        video.likes.add(user)
    return HttpResponseRedirect(
        reverse('water:video', args=(video.id,))
    )


def gallery_show(request):
    gallery = Gallery.objects.all()
    paginator = Paginator(gallery, 12)  # 3 * 4
    page = request.GET.get('page')
    try:
        gallery = paginator.page(page)
    except PageNotAnInteger:
        gallery = paginator.page(1)
    except EmptyPage:
        gallery = paginator.page(paginator.num_pages)
    context = {
        'gallery': gallery,
    }
    return render(request, 'water/gallery.html', context)


def subscribe_event(request, id):
    user = get_object_or_404(User, id=request.user.id)
    event = get_object_or_404(Event, id=id)
    if user in event.objects.all():
        event.users.remove(user)
    else:
        event.users.add(user)
    return HttpResponseRedirect(
        reverse('water:feed', args=(event.id,))
    )


def video_show(request):
    context = {
        'video': Videos.objects.all(),
    }
    if request.is_ajax():
        return render(request, 'water/ajvideo.html', context)
    else:
        return render(request, 'water/video.html', context)