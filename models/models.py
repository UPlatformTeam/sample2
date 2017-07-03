from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
	thumbnail = models.ImageField(upload_to='img/thumbnail/')
	image = models.ImageField(upload_to='img/')
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=1023)
	price = models.IntegerField()
	status = models.CharField(max_length=255)
	is_visible = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class order(models.Model):
	user = models.ForeignKey(User)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()
	datetime = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=255)

	def __str__(self):
		return self.user.username

class git_repository(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=127)
	full_name = models.CharField(max_length=1023)
	is_connected = models.BooleanField(default=False)


class repository_update(models.Model):
	user = models.ForeignKey(User)
	started_at = models.DateTimeField(auto_now=True)
	is_processed = models.BooleanField(default=False)