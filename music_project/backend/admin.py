from django.contrib import admin

# Register your models here.
from backend.models import (Album,Artist,Song)



class AdminArtist(admin.ModelAdmin):

	class Meta:
		model=Artist

	list_display=['name']


class AdminAlbum(admin.ModelAdmin):

	class Meta:
		model=Album

	list_display=['title','artist']


class AdminSong(admin.ModelAdmin):

	class Meta:
		model=Song

	list_display=['song_name','album','get_artist']

	def get_artist(self,obj):
		return obj.album.artist
	get_artist.short_description='Artist'
	get_artist.admin_order_field='album__artist'

admin.site.register(Artist,AdminArtist)
admin.site.register(Album,AdminAlbum)
admin.site.register(Song,AdminSong)