from django.db import models
from django.utils import timezone

# Create your models here.

class Seed(models.Model):
		name = models.CharField(max_length=32)
		info = models.CharField(max_length=128)
		link = models.TextField(blank=True, null=True)
		selfcontent = models.IntegerField(default=1)
		created_date = models.DateTimeField(default=timezone.now)
		published_date = models.DateTimeField(blank=True, null=True)

		def __str__(self):
				return self.name

class Flower(models.Model):	
		name = models.CharField(max_length=256)
		info = models.TextField(blank=True, null=True)
		link = models.ManyToManyField(Seed)
		created_date = models.DateTimeField(default=timezone.now)
		published_date = models.DateTimeField(blank=True, null=True)

		def publish(self):
				self.published_date = timezone.now()
				self.save()

		def __str__(self):
				return self.name

		def info_flower(self):
				return self.info

class Honeycomb(models.Model):
		name = models.CharField(max_length=32)

		def __str__(self):
				return self.name

class Honey(models.Model):
		name = models.CharField(max_length=32)
		info = models.TextField(blank=True, null=True)
		flowers = models.ManyToManyField(Flower)
		honeycomb = models.ForeignKey(Honeycomb)
		created_date = models.DateTimeField(default=timezone.now)
		published_date = models.DateTimeField(blank=True, null=True) 

		def publish(self):
				self.published_date = timezone.now()
				self.save()
  
		def __str__(self):
				return self.name
