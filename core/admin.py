from django.contrib import admin

# Register your models here.
from .models import Expense, CategoryExpense

admin.site.register(Expense)
admin.site.register(CategoryExpense)