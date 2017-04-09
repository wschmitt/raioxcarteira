from __future__ import unicode_literals

from django.forms import ModelForm
from django.db import models
from django.utils import timezone

# Create your models here.
class Expense(models.Model):
	user = models.ForeignKey('auth.User')
	post_date = models.DateTimeField()
  	date = models.DateTimeField(blank=True, null=True)
  	category = models.ForeignKey('CategoryExpense')
  	description = models.CharField(max_length=500)
	value = models.FloatField()

	def Save(self):
		self.post_date = timezone.now()
		self.save()

	def __str__(self):
		return self.description

class CategoryExpense(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class ExpenseForm(ModelForm):
	class Meta:
		model = Expense
		fields = ['date', 'category', 'description', 'value']

#class CategoryExpenseForm(ModelForm):
#	class Meta:
#		model = CategoryExpense
#		fields = ['name']
