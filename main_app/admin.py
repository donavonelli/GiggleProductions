from django.contrib import admin
from .models import Newsletter

# Register your models here.
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email',)


admin.site.register(Newsletter, NewsletterAdmin)