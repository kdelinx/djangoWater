# coding: utf-8
from users.models import User


def site_static(request):
    context = {
        'sum_users': User.objects.all().count(),
        'sum_victims': User.objects.order_by('-score_die')[:5],
    }
    return context