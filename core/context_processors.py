from django.conf import settings
from core.models import Page


def site_meta(request):
    article = Page.objects.all()
    context = {
        'project_name': settings.PROJECT_NAME,
        'project_desc': settings.PROJECT_DESC,
        'project_time': settings.PROJECT_TIME,
        'project_phone': settings.PROJECT_PHONE,
        'project_place': settings.PROJECT_PLACE,
        'article': article,
    }
    return context