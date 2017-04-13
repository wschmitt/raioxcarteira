from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.
from .models import Expense, CategoryExpense, ExpenseForm, CategoryExpenseForm
from .sites import my_admin_site

#class ExpenseAdmin(ModelAdmin):
#    form = ExpenseForm

#class ExpenseModelAdmin(ModelAdmin):
#    form = ExpenseForm

#my_admin_site.register(Expense, ModelAdmin)
#my_admin_site.register(CategoryExpense, ModelAdmin)
# class ExpenseAdmin(admin.ModelAdmin):
#     form = ExpenseForm

#     def __init__(self, model, admin_site):
#         super(ExpenseAdmin,self).__init__(model,admin_site)
#         self.form.admin_site = admin_site # capture the admin_site


# Register both models to our custom admin site
# my_admin_site.register(CategoryExpense, ModelAdmin)
# my_admin_site.register(Expense, ExpenseAdmin)

#my_admin_site.register(Expense, ExpenseAdmin)


# class TestInline(admin.TabularInline):
#     form = CategoryExpenseForm
#     model = CategoryExpense
#     fk_name = 'name'


class ExpenseAdmin(admin.ModelAdmin):
    form = ExpenseForm
    
    # inlines = [TestInline]

admin.site.register(CategoryExpense)
admin.site.register(Expense, ExpenseAdmin)


# Register both models to our custom admin site
#admin.site.register(Expense)
#admin.site.register(CategoryExpense)