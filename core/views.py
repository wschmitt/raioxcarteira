from django.shortcuts import render
from django.views import generic
from .models import Expense, ExpenseForm, CategoryExpense, CategoryExpenseForm, options_expense_receipt
from django.forms import modelformset_factory, formset_factory
from dal import autocomplete
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Sum

try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy


# Create your views here.
def home(request):
	month = int(request.GET.get('month', 0))
	#print month, type(month), int(month), type(int(month))
	this_month = timezone.now().month + month
	#print timezone.now().month, timezone.now().month + month, month
	expenses = Expense.objects.filter(user=request.user, date__month=this_month, entry_type=options_expense_receipt['despesa'])
	receipts = Expense.objects.filter(user=request.user, date__month=this_month, entry_type=options_expense_receipt['receita'])
	#print expenses
	total_expent = (expenses.aggregate(Sum('value')))['value__sum'] or 0
	total_receipt = (receipts.aggregate(Sum('value')))['value__sum'] or 0
	remainder = total_receipt - total_expent

	#compute graph data
	expenses_chart_data = {}
	receipts_chart_data = {}
	categories = {x.id: x.name for x in CategoryExpense.objects.filter(user=request.user)}

	#print categories
	for cat_id, cat_name in categories.iteritems():
		total_expense = (expenses.filter(category=cat_id).aggregate(Sum('value')))['value__sum'] or 0
	 	expenses_chart_data[cat_name] = total_expense
	 	total_receipt = (receipts.filter(category=cat_id).aggregate(Sum('value')))['value__sum'] or 0
	 	receipts_chart_data[cat_name] = total_receipt
	
	#js = json.dumps(expenses_chart_data)
	print receipts_chart_data
	return render(request, 'core/index.html', {
		'total_expent':total_expent,
		'total_receipt':total_receipt,
		'remainder':remainder,
		'expenses_chart_data':expenses_chart_data,
		'receipts_chart_data':receipts_chart_data,
		})

def despesas(request):

	ExpenseFormSet = modelformset_factory(Expense, form=ExpenseForm, extra=1, can_delete=True)
	if (request.method == 'POST'):
		#print request.POST
		formset = ExpenseFormSet(request.POST)
		if formset.is_valid():
			#print formset
			instances = formset.save(commit=False)
			for obj in formset.deleted_objects:
				obj.delete()
			for instance in instances:
				instance.user = request.user
				instance.post_date = timezone.now()
				print instance.entry_type
				instance.save()
		else:
			print formset.errors

		return HttpResponseRedirect('/despesas')
	month = int(request.GET.get('month', 0))
	this_month = timezone.now().month + month
	formset = ExpenseFormSet(queryset=Expense.objects.filter(user=request.user,date__month=this_month).order_by('date'))
	#print formset
	return render(request, 'core/despesas.html', {'formset' : formset})

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