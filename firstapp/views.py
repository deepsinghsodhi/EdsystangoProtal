from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from firstapp.forms import signup
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from firstapp.models import EdsysClass, Subject, InstituteInfo, Student, Employee, Income, Expense, Attendance, StudentAttendance
from django.urls import reverse
from django.db.models import Q, Sum
# Create your views here.


# Default Login Page
def first_login_page(request):
    return HttpResponseRedirect('/accounts/login')

def signup_view(request):
    sform = signup()
    if request.method == "POST":
        sform = signup(request.POST)
        if sform.is_valid():
            data = sform.save(commit = False)
            data.set_password(data.password)
            data.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'firstapp/signup.html', {'sform':sform})

@login_required
def dashboard_view(request):
    count_student = Student.objects.all().count()
    count_employee = Employee.objects.all().count()
    income_sum = list(Income.objects.aggregate(Sum('income_amount')).values())[0]  #sum of income amount.
    expense_sum = list(Expense.objects.aggregate(Sum('expense_amount')).values())[0]
    return render(request, 'firstapp/dashboard.html', {'count_student':count_student, 'count_employee':count_employee, 'income_sum':income_sum, 'expense_sum':expense_sum})

# institute information view
class InstituteInfoView(ListView):
    model = InstituteInfo
    template_name = 'firstapp/instituteinfoview.html'
    def get_success_url(self):
        return reverse('institute info')

# adding new institute information
class InsertInstituteInfo(CreateView):
    model = InstituteInfo
    fields = '__all__'
    def get_success_url(self):
        return reverse('institute info')

# Updating INSTITUTE Information
class UpdateInfo(UpdateView):
    model = InstituteInfo
    fields = '__all__'
    def get_success_url(self):
        return reverse('institute info')


# Adding New Class
@method_decorator(login_required, name='dispatch')
class AddClass(CreateView):
    model = EdsysClass
    fields = '__all__'
    def get_success_url(self):
        return reverse('add class')

# Display all classes
class AllClass(ListView):
    model = EdsysClass
    template_name = 'firstapp/allclass.html'
    context_object_name = 'classes'

# Update form of a class
@method_decorator(login_required, name='dispatch')
class UpdateClass(UpdateView):
    model = EdsysClass
    fields = '__all__'
    def get_success_url(self):
        return reverse('view class')

# Edit or delete a Class
@method_decorator(login_required, name='dispatch')
class EditDeleteClass(ListView):
    model = EdsysClass
    template_name = 'firstapp/edit-delete_view.html'
    context_object_name = 'classes'

# deleting a class with its ID
@login_required
def DeleteClass(request, id):
    mydict = {'msg':'Class Deleted'}
    del_class = EdsysClass.objects.get(id=id)
    del_class.delete()
    del_class = EdsysClass.objects.all()
    return HttpResponseRedirect("/editdelete/")
    # return render (request, 'firstap/edit-delete_view.html', {'del_class':del_class})

# adding New subject to class
@method_decorator(login_required, name='dispatch')
class InsertSubject(CreateView):
    model = Subject
    fields = '__all__'
    def get_success_url(self):
        return reverse('all_subject')
# def SubjectList(request):
#     subjects = Subject.objects.all()
#     return render (request, 'firstapp/subjectlist.html', {'subjects':subjects})

        # list of all subjects
def SubjectList(request):
    subjects = EdsysClass.objects.all()
    return render(request,'firstapp/subjectlist.html',{'subjects':subjects})


                #<<<<<<<<<<<<<<<<<<<<-----------SEARCH---------.>>>>>>>>>>>>>>>
                # Search bar for student--- its can be search by its Registration Number, Name and id
def SearchStudent(request):

    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Student.objects.filter(Q(stu_name__icontains=srch) | Q(registration_num__icontains=srch))
            if match:
                return render(request, 'firstapp/allstudent.html', {'sr':match})
            else:
                # messages.error(request, 'no result found')
                return HttpResponseRedirect('/searchstudent/')
        else:
            return HttpResponseRedirect('/searchstudent/')
    return render(request, 'firstapp/allstudent.html')


                # STUDENT section start----------------------->>>>>>>>>

# VIEW ALL STUDENTS-------------------->>>>>>>>>>>>>>>>>>...
@method_decorator(login_required, name='dispatch')
class AllStudent(ListView):
    model = Student
    template_name = 'firstapp/allstudent.html'
    context_object_name = 'students'

            # student detail view with its complete personal infomation
@method_decorator(login_required, name='dispatch')
class StudentDetailView(DetailView):
    model = Student
    template_name = 'firstapp/studentdetailview.html'
    context_object_name = 'student_details'

# add student CBV ----->>>>>>>>
@method_decorator(login_required, name='dispatch')
class AddStudent(CreateView):
    model = Student
    fields = '__all__'
    # template_name = 'firstap/addstudent.html'
    def get_success_url(self):
        return reverse('view student')

# Update/delete student view CBV ----->>>>>>>>
@method_decorator(login_required, name='dispatch')
class EditDeleteStudent(ListView):
    model = Student
    template_name = 'firstapp/edit-delete_student.html'
    context_object_name = 'students'

# Updae student CBV ----->>>>>>>>
@method_decorator(login_required, name='dispatch')
class UpdateStudent(UpdateView):
    model = Student
    fields = '__all__'
    def get_success_url(self):
        return reverse('view student')

        # deleting student by its id FBV ----->>>>>>>>
def DeleteStudent(request, id):
    mydict = {'msg':'Student Data Deleted'}
    del_student = Student.objects.get(id=id)
    del_student.delete()
    del_student = Student.objects.all()
    return HttpResponseRedirect("/viewallstudent/")

        # Admission letter view
@method_decorator(login_required, name='dispatch')
class AdmissionLetterView(ListView):
    model = Student
    template_name = 'firstapp/admissionletterview.html'
    context_object_name = 'letterview'

            # Display Admission letter of student
@method_decorator(login_required, name='dispatch')
class AdmissionLetter(DetailView):
    model = Student
    template_name = 'firstapp/admission-letter.html'
    context_object_name = 'admissionletter'

                # <<<<<<<<<<<<<<<<<------------------# EMPLOYEE section---------------------------->>>>>>>>>>>>>>>>>

                # employe search bar-- it will search with its ID, Name and Its employee type--
def SearchEmployee(request):

    if request.method == 'POST':
        srch = request.POST['search_emp']

        if srch:
            match = Employee.objects.filter(Q(emp_name__icontains=srch) | Q(emp_type__icontains=srch))
            if match:
                return render(request, 'firstapp/allemp.html', {'srchemp':match})
            else:
                # messages.error(request, 'no result found')
                return HttpResponseRedirect('/viewallemployee/')
        else:
            return HttpResponseRedirect('/viewallemployee/')
    return render(request, 'firstapp/allemp.html')

            # Display All employe Name and basic detail as a list view
@method_decorator(login_required, name='dispatch')
class AllEmp(ListView):
    model = Employee
    template_name = 'firstapp/allemp.html'
    context_object_name = 'employees'

            # Adding new employe form
@method_decorator(login_required, name='dispatch')
class AddEmployee(CreateView):
    model = Employee
    fields = '__all__'
    # template_name = 'firstap/addemployee.html'
    def get_success_url(self):
        return reverse('view_employee')

                # Employee's updationg View CBV
@method_decorator(login_required, name='dispatch')
class EditDeleteEmployee(ListView):
    model = Employee
    fields = '__all__'
    template_name = 'firstapp/edit-delete_employee.html'
    context_object_name = 'employees'
    def get_success_url(self):
        return reverse('view_employee')

            # Employee Detail view including its all personal informations
@method_decorator(login_required, name='dispatch')
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'firstapp/employeedetailview.html'
    context_object_name = 'employee_details'


            # Update an Employee's data by its ID(function Based View)
@method_decorator(login_required, name='dispatch')
class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    def get_success_url(self):
        return reverse('view_employee')

            # Delete an Employee's data by its ID(function Based View)
def DeleteEmployee(request, id):
    mydict = {'msg':'Employee Data Deleted'}
    delete_employee = Employee.objects.get(id=id)
    delete_employee.delete()
    delete_employee = Employee.objects.all()
    return HttpResponseRedirect("/viewallemployee/")
# --------------------------------------------------------------------------



            # ACCOUNTS SECTION STARTED-------------------=>>>>>>>>>>>>>>>>>>>>>>>>
                    #Income form
@method_decorator(login_required, name='dispatch')
class AddIncome(CreateView):
    model = Income
    fields = '__all__'
    template_name = 'firstapp/addincome.html'
    def get_success_url(self):
        return reverse('add_income')

                #Expenses form
@method_decorator(login_required, name='dispatch')
class AddExpense(CreateView):
    model = Expense
    fields = '__all__'
    template_name = 'firstapp/addexpense.html'
    def get_success_url(self):
        return reverse('add_expense')


            #  Account Statement View By function based
def Balance(request):
    income_obj = Income.objects.all()
    expense_obj = Expense.objects.all()
    income_sum = list(Income.objects.aggregate(Sum('income_amount')).values())[0]  #sum of income amount.
    expense_sum = list(Expense.objects.aggregate(Sum('expense_amount')).values())[0]
    return render(request, 'firstapp/statement.html', {'income_obj':income_obj, 'expense_obj':expense_obj, 'income_sum':income_sum, 'expense_sum':expense_sum})
# ---------------------------------------------------------------------------------

                    #--------------------- ATTENDANCE SECTION------------------------------

# class StudentAttend(ListView):
#     model = EdsysClass
#     template_name = 'firstapp/studentattend.html'
#     context_object_name = 'classes'

# def StudentAttend(request):
#     queryset = Student.objects.all()
#     def get_queryset(self):
#         queryset = Student.objects.all()
#         if self.request.GET.get("classes"):
#             selection = self.request.GET.get("classes")
#             if selection == "python":
#                 queryset = Student.objects.all()
#         return render(request, 'firstapp/studentattend.html', {'queryset':queryset})
#
# def AllClassAttendanceView(request):
#     classes = EdsysClass.objects.all()
#     return render(request, 'firstapp/allattendance.html', {'classes':classes})

def AllClassAttendance(request):
    classes = EdsysClass.objects.all()
    if request.method == 'POST' and 'search' in request.POST:
        dropdown_val = request.POST.get('dropdownlist')
        return HttpResponseRedirect("/studentattendance"+dropdown_val)
    return render(request, 'firstapp/allattendance.html', {'classes':classes})

# def AttendanceClass(request, pk):
#     allclass = EdsysClass.objects.get(id=pk)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         id = request.POST.get('id')
#         classto = 'java'
#         val = request.POST.get('x')
#         form = Attendance(date=date, Class=classto, StudentName=name, status=val)
#         form.save()
#     return render(request, 'firstapp/studentattendance.html', {'allclass':allclass})

def StudentAttendance(request, pk):

    allclass = EdsysClass.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        classto = 'java'
        val = request.POST.get('x')
        form = Attendance(date=date, Class=classto, StudentName=name, status=val)
        form.save()
        # print(id, name, classto)
    return render(request, 'firstapp/studentattendance.html', {'allclass':allclass})


class EmployeeAttend(ListView):
    model = Employee
    template_name = 'firstapp/employeeattend.html'
    context_object_name = 'employees'
