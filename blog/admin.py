from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','id','author','published','post_categories')
    ordering = ('author','published')
    search_fields = ('title','content','author__username','categories__name')
    date_hierarchy = 'created'
    list_filter = ('author__username','categories__name')

    def post_categories(self,obj):
        return ",".join([c.name for c in obj.categories.all().order_by("name")])

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)