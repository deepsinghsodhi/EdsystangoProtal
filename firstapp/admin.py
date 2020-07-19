from django.contrib import admin
from firstapp.models import EdsysClass, Subject, InstituteInfo, Student, Employee, Income, Expense, StudentAttendance, Attendance
# Register your models here.

class ExpenseAdminPage(admin.ModelAdmin):
    list_display = ['expense_description', 'expense_date', 'expense_amount']
    fields = ['expense_description', 'expense_amount', 'expense_date']  #Field Ordering in Admin panel
    search_fields = ['expense_description', 'expense_amount']
    list_fiter = ['expense_description']
    list_editable = ['expense_amount']

class IncomeAdminPage(admin.ModelAdmin):
    list_display = ['income_description', 'income_date', 'income_amount']
    fields = ['income_description', 'income_amount', 'income_date'] #Field Ordering in Admin panel
    search_fields = ['income_description', 'income_amount']
    list_fiter = ['income_description']
    list_editable = ['income_amount']


admin.site.register(InstituteInfo)
admin.site.register(EdsysClass)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(StudentAttendance)
admin.site.register(Attendance)

admin.site.register(Income, IncomeAdminPage)
admin.site.register(Expense, ExpenseAdminPage)
