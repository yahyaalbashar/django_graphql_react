import graphene

from graphene_django import DjangoObjectType

from backend.models import (Artist,Album,Song)


class ArtistType(DjangoObjectType):
	class Meta:
		model=Artist


class AlbumType(DjangoObjectType):
	class Meta:
		model=Album


class SongType(DjangoObjectType):

	class Meta:
		model=Song


class Query(object):
	artists= graphene.List(ArtistType)

	albums= graphene.List(AlbumType)

	songs= graphene.List(SongType)


	def resolve_artists(self,info,**kwargs):
		
		return Artist.objects.all()

	def reslove_albums(self,info,**kwrgs):
		return Album.objects.all()

	def resolve_songs(self,info,**kwargs):
		return Song.objects.all()
