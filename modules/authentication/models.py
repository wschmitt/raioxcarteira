from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Entry(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

	def publish(self):
		self.save()
		
	def __str__(self):
		return self.name

#	login = models.CharField(max_length=100)
# class User(models.Model):
#     login = models.CharField(max_length=100)
#     password = 
#     #author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title
