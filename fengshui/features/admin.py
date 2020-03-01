from django.contrib import admin
from .models import RegUser, Direction, Membership

# Register your models here.
admin.site.register(RegUser)
admin.site.register(Direction)
admin.site.register(Membership)
