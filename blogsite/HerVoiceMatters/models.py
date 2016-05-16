from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Event(models.Model):

	title = models.CharField(max_length = 200 ,default= " ")
	organizer = models.ForeignKey(User,default=1)
	event_date = models.DateTimeField(blank = False)
	location = models.CharField(max_length = 150,blank = False, null = False)
	description = models.TextField(max_length = 800)
	height_img = models.IntegerField(default = 0)
	width_img = models.IntegerField(default = 0)
	image_field = models.ImageField(upload_to ="events/",
		      null = True,
		      blank = True,
		      width_field = 'width_img',
		      height_field = "height_img",
		)
	Attending = models.IntegerField(default = 0)

	class Meta:
		ordering = ['-event_date']


class Gallery(models.Model):
	height_img = models.IntegerField(default = 0)
	width_img = models.IntegerField(default = 0)
	image_field = models.ImageField(upload_to ="gallery/",
		      null = True,
		      blank = True,
		      width_field = 'width_img',
		      height_field = "height_img",
		)
	description= models.CharField(max_length = 300)	
	created_date = models.DateTimeField(default = timezone.now)

	class Meta:
		ordering = ["-created_date"]


class Post(models.Model):
	POST_CATEGORY = (
		('fas','FASHION'),
		('food','FOOD'),
		('girl','GIRL TALK'),
		) 

	author = models.ForeignKey(User,default=1)
	title = models.CharField(max_length = 200)
	category = models.CharField(max_length= 5, choices = POST_CATEGORY, default= 'girl')
	content = models.TextField()
	height_img = models.IntegerField(default = 0)
	width_img = models.IntegerField(default = 0)
	image_field = models.ImageField(upload_to ="posts/",
		      null = True,
		      blank = True,
		      width_field = 'width_img',
		      height_field = "height_img",
		)

	created_date = models.DateTimeField(default = timezone.now)

	def __str__(self):                  
		return self.title

	def get_absolute_url(self):
		return reverse ('posts:detail', kwargs ={'id':self.id})
	class Meta:
		ordering = ["-created_date"]






