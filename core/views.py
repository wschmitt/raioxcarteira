from django.shortcuts import render
from .models import Expense, ExpenseForm
from django.forms import modelformset_factory

# Create your views here.
def home(request):
	#print type(CategoryExpenseForm)
	#form = ExpenseForm()
	# Create the formset, specifying the form and formset we want to use.
	formset = modelformset_factory(Expense, form=ExpenseForm)
	return render(request, 'core/index.html', {'formset' : formset})

def about(request):
	return render(request, 'core/about.html', {})