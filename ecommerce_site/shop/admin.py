from django.contrib import admin
from .models import AboutVideo
from  .models import Image
from .models import Pics 
from .models import Iphone
from django.contrib import admin

from django.contrib import admin
from .models import ContactMessage

admin.site.register(AboutVideo)
admin.site.register(Image)
admin.site.register(Pics)


@admin.register(Iphone)
class IphoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'caption1')




@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')

