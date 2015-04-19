from django.contrib import admin
from blog.models import Category, Entries, Comment
# Register your models here.

#admin.site.register(TagModel)
#admin.site.register(Category)
#admin.site.register(Comment)
#admin.site.register(Entries)



class CategoryAdmin(admin.ModelAdmin):
	list_display=['id','title']
	list_display_links=['id','title']


class EntriesAdmin(admin.ModelAdmin):
	list_display=['id','title','created','text','Comment','category']
	list_filter=['category']
	list_display_links=['id','title']
	search_fields=['title','category']
	ordering=['-created']

class CommentAdmin(admin.ModelAdmin):
	list_display=['id','name','text','password','created','entry']
	list_filter=['entry']
	list_display_links=['id','entry']
	search_fields=['name']
	ordering=['-created']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Entries,EntriesAdmin)
admin.site.register(Comment,CommentAdmin)
