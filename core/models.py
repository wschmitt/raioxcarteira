from __future__ import unicode_literals

from dal import autocomplete
from django import forms
from django.forms.widgets import DateInput, CheckboxInput
# from django.core.urlresolvers import reverse

from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
#import floppyforms.__future__ as floppyforms
from django.db import models
from django.utils import timezone

#from django.contrib import admin
from .sites import my_admin_site

#from .widgets import CustomRelatedFieldWidgetWrapper
#from django.contrib import admin
options_expense_receipt = {'despesa':True, 'receita':False}

# Create your models here.
class Expense(models.Model):
	user = models.ForeignKey('auth.User')
	post_date = models.DateTimeField(auto_now=True, blank=True, null=True)
  	date = models.DateField(blank=True, null=True)
  	category = models.ForeignKey('CategoryExpense', null=True, blank=True, on_delete=models.SET_NULL)
  	description = models.CharField(max_length=500)
  	entry_type = models.BooleanField(default=True) # True -> despesa, False -> receita
	value = models.FloatField()

	def Save(self):
		self.post_date = timezone.now()
		print 'saving...'
		self.save()

	def __unicode__(self):
		return str(self.id)

class CategoryExpense(models.Model):
	user = models.ForeignKey('auth.User', null=True)
	name = models.CharField(max_length=50);
	def __unicode__(self):
		return self.name

class ExpenseForm(forms.ModelForm):
	#def __init__(self):
	#	self.fields['entry_type'].initial = True
	#class Media:
	#	css = { 'all':'css/widgets.css'}
	#	js = ('admin/js/admin/RelatedObjectLookups.js')
	date = forms.DateField(input_formats=['%d/%m/%Y','%d/%m/%y'], widget=forms.DateInput(format='%d/%m/%Y'))
	entry_type = forms.BooleanField(initial=True, required=False, widget=CheckboxInput(attrs={'data-on':'Despesa', 'data-off':'Receita', 'data-toggle': 'toggle',
    			'data-onstyle':'danger', 'data-offstyle':'success', }))
	class Meta:
		model = Expense
		fields = ['date', 'category', 'description', 'value', 'entry_type']
		widgets = {
        	'category': autocomplete.ModelSelect2(url='select2_fk'),#attrs={'data-html': 'true', 'data-placeholder': 'Autocomplete ...',})
    		#'entry_type': CheckboxInput(attrs={#'data-toggle': 'toggle', 'data-on':'Despesa', 'data-off':'Receita',
    			#'data-onstyle':'danger', 'data-offstyle':'success', 
    	}
    	
			
    

class CategoryExpenseForm(forms.ModelForm):
	class Meta:
		model = CategoryExpense
		fields = ['user', 'name']
		widgets = {
			'name' : autocomplete.ModelSelect2(url='select2_fk2')
		}
