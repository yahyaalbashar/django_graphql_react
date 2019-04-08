from django.db import models

# Create your models here.


class Album(models.Model):
	title=models.CharField(max_length=255)

	artist=models.ForeignKey('Artist',on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Artist(models.Model):
	name=models.CharField(max_length=255)


	def __str__(self):
		return self.name


class Song(models.Model):
	song_name=models.CharField(max_length=255)
	album=models.ForeignKey(Album,on_delete=models.CASCADE)

	def __str__(self):
		return self.song_name

