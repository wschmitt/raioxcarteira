from django.shortcuts import render
from django.views import generic
from .models import Expense, ExpenseForm, CategoryExpense, CategoryExpenseForm
from django.forms import modelformset_factory
from django.forms import inlineformset_factory
from dal import autocomplete

try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy

# Create your views here.
def home(request):
	#print type(CategoryExpenseForm)
	#form = ExpenseForm()
	# Create the formset, specifying the form and formset we want to use.
	
	formset = modelformset_factory(Expense, form=ExpenseForm, extra=0, can_delete=True)
	form = ExpenseForm()
	return render(request, 'core/index.html', {'formset' : formset, 'form' : form})

def about(request):
	return render(request, 'core/about.html', {})

class UpdateView(generic.UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'core/teste.html'
    success_url = reverse_lazy('teste')

    def get_object(self):
        return Expense.objects.first()

    def form_valid(self, form):
		print ('VIEW BEING UPDATE, USER: ' + self.request.user)
		form.instance.user = self.request.user
		return super(UpdateCategoryView, self).form_valid(form)



class UpdateCategoryView(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		if not self.request.user.is_authenticated():
			return CategoryExpense.objects.none()

		qs = CategoryExpense.objects.filter(user=self.request.user)
		if self.q:
			qs = qs.filter(name__istartswith=self.q)
		return qs
	def create_object(self, text):
		#print({self.create_field: text, 'user' : self.request.user})
		return self.get_queryset().create(**{self.create_field: text, 'user' : self.request.user})
		#return super(UpdateCategoryView, self).create_object(text)