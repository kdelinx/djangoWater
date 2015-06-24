from django.contrib import admin
from users.models import Static, User
from django.contrib.auth.models import Group


admin.site.register(User)
admin.site.register(Static)
admin.site.unregister(Group)
