from django.contrib import admin
from .models import Post,Tags,Tweets
# Register your models here.

class TagInline(admin.StackedInline):
    model = Tags
class TweetInline(admin.StackedInline):
    model = Tweets
class PostAdmin(admin.ModelAdmin):
    inlines = [TagInline,TweetInline]
admin.site.register(Post,PostAdmin)

