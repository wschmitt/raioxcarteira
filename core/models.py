from __future__ import unicode_literals

from dal import autocomplete
from django.forms import ModelForm
# from django.contrib.admin.widgets import FilteredSelectMultiple
# from django.core.urlresolvers import reverse

from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
#import floppyforms.__future__ as floppyforms
from django.db import models
from django.utils import timezone

#from django.contrib import admin
from .sites import my_admin_site

#from .widgets import CustomRelatedFieldWidgetWrapper
#from django.contrib import admin

# Create your models here.
class Expense(models.Model):
	user = models.ForeignKey('auth.User')
	post_date = models.DateTimeField(blank=True, null=True)
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
	user = models.ForeignKey('auth.User', null=True)
	name = models.CharField(max_length=50);
	def __str__(self):
		return self.name

class ExpenseForm(ModelForm):
	#class Media:
	#	css = { 'all':'css/widgets.css'}
	#	js = ('admin/js/admin/RelatedObjectLookups.js')
	class Meta:
		model = Expense
		fields = ['date', 'category', 'description', 'value']
		widgets = {
        	'category': autocomplete.ModelSelect2(url='select2_fk')#attrs={'data-html': 'true', 'data-placeholder': 'Autocomplete ...',})
    	} 
			
    

class CategoryExpenseForm(ModelForm):
	class Meta:
		model = CategoryExpense
		fields = ['user', 'name']
		widgets = {
			'name' : autocomplete.ModelSelect2(url='select2_fk2')
		}
