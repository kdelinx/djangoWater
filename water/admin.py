from django.contrib import admin
from water.models import Event, News, Gallery, Videos


class VideoInline(admin.TabularInline):
    model = Videos
    fk_name = 'news'


class RVideoAdmin(admin.ModelAdmin):
    # inlines = [VideoInline]
    save_on_top = True


admin.site.register(Event)
admin.site.register(News)
admin.site.register(Gallery)
admin.site.register(Videos, RVideoAdmin)