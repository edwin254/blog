from django.contrib import admin
from .models import Post,Event , Gallery

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	date_hierachy = 'created_date'
	list_display = ["author","title","category","created_date",]
	list_display_links = ["title"]
	search_fields = ["title", "content"]

	class Meta:
		model = Post

class EventAdmin(admin.ModelAdmin):
	date_hierachy = ["event_date"]
	list_display = ["organizer", "title","location","Attending"]
	class Meta:
		model = Event

class GalleryAdmin(admin.ModelAdmin):
	date_hierachy = ["created_date"]
	list_display = ["description", "created_date"]
	class Meta:
		model = Gallery

admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Gallery, GalleryAdmin)
