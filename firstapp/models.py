from django.db import models
from django.urls import reverse
# Create your models here.

class EdsysClass(models.Model):
    name = models.CharField(max_length = 50)
    fee = models.IntegerField()
    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse ('add class')

class Subject(models.Model):
    marks = models.IntegerField()
    sub_category = models.CharField(max_length=30)
    class_name = models.ForeignKey(EdsysClass, on_delete=models.CASCADE)
    def __str__(self):
        return self.sub_category
    # def get_absolute_url(self):
    #     return reverse ('add sub')

class InstituteInfo(models.Model):
    institutename = models.CharField(max_length=50)
    targetline = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=50, default="")
    website = models.CharField(max_length=200)
    address = models.TextField()
    logo = models.FileField(upload_to = 'images', default='student_icon.png')
    def __str__(self):
        return self.institutename
    # def get_absolute_url(self):
    #     return reverse ('institute info')

class Student(models.Model):
    GENDER_CHOICES = (('male','Male'),('female','Female'),('other','Other'))
    RELIGION_CHOICES = (('buddhism','Buddhism'),('christianity','Christianity'),('hinduism','Hinduism'),('islam','Islam'),('jainism','Jainism'),('sikhism','Sikhism'),('other','Other'))
    stu_name = models.CharField(max_length = 30)
    registration_num = models.IntegerField()
    email = models.CharField(max_length=50, default="")
    Admission_date = models.DateField()
    photo = models.FileField(upload_to = "images",default = "student_icon.png")
    mobile_num = models.IntegerField(null=False, blank=False, unique=True)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = "male")
    caste = models.CharField(max_length = 30)
    previous_school = models.CharField(max_length = 50)
    orphan_student = models.BooleanField(blank = True)
    religion = models.CharField(max_length = 20,choices = RELIGION_CHOICES,default = "hinduism")
    address = models.TextField()
    father_name = models.CharField(max_length = 20)
    father_education = models.CharField(max_length = 20,null=True, blank=True)
    father_occupation = models.CharField(max_length = 20,null=True, blank=True)
    father_income = models.FloatField(null=True, blank=True)
    father_mobile = models.IntegerField()
    mother_name = models.CharField(max_length = 20)
    mother_education = models.CharField(max_length = 20,null=True, blank=True)
    mother_occupation = models.CharField(max_length = 20,null=True, blank=True)
    mother_income = models.FloatField(null=True, blank=True)
    mother_mobile = models.IntegerField(null=True, blank=True)
    name_of_class = models.ForeignKey(EdsysClass,on_delete = models.CASCADE)
    def __str__(self):
        return self.stu_name
    # def get_absolute_url(self):
    #     return reverse('students list')

class Employee(models.Model):
    emp_name = models.CharField(max_length = 30)
    joining_date = models.DateField(auto_now=False, auto_now_add=False)
    EMP_TYPE_CHOICES = (('---Employee Type---','---Employee Type---'),('Teaching Staff','Teaching Staff'),('Non-Teaching','Non-Teaching'))
    emp_type = models.CharField(max_length = 20,choices = EMP_TYPE_CHOICES,default = "---Employee Type---")
    mobile_num = models.IntegerField()
    salary = models.IntegerField()
    emp_photo = models.FileField(upload_to = "images",default = "employee_icon.png")
    def __str__(self):
        return self.emp_name

class Income(models.Model):
    income_date = models.DateField(auto_now=False, auto_now_add=False)
    income_amount = models.IntegerField()
    income_description = models.TextField()
    def __str__(self):
        return self.income_description

class Expense(models.Model):
    expense_date = models.DateField(auto_now=False, auto_now_add=False)
    expense_amount = models.IntegerField()
    expense_description = models.TextField()
    def __str__(self):
        return self.expense_description

class StudentAttendance(models.Model):
    attendance_choices = (('present', 'present'), ('absent', 'absent'), ('leave', 'leave'))
    date = models.DateField()
    Class = models.ForeignKey(EdsysClass, on_delete=models.CASCADE)
    StudentName = models.ForeignKey(Student, on_delete=models.CASCADE)
    Attendance = models.CharField(max_length = 20, choices = attendance_choices,)

class Attendance(models.Model):
    date = models.DateField()
    Class = models.CharField(max_length=50)
    StudentName = models.CharField(max_length = 50)
    status = models.CharField(max_length=20)
    def __str__(self):
        return (self.StudentName)

class FeeSubmission(models.Model):
    FeeDate = models.DateField()
    RegistrtionId = models.IntegerField()
    StudentName = models.CharField(max_length=255)
    StudentClass = models.CharField(max_length=255)
    MonthlyFee = models.IntegerField()
    AdmissionFee =models.IntegerField()
    RegistrtionFee = models.IntegerField()
    PreviousBalance = models.IntegerField()
    DiscountFee = models.IntegerField()
    Total = models.IntegerField()
    Deposit = models.IntegerField()
    DueBalance = models.IntegerField()
    def __str__(self):
        return (self.StudentName)
