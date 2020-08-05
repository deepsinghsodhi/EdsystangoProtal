
from django.contrib import admin
from django.urls import path, include
from firstapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard_view),
    path('', views.first_login_page),             #Default Login Page
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view),
    path('addclass/', views.AddClass.as_view(), name='add class'),  # Add Class CBV
    path('viewallclass/', views.AllClass.as_view(), name='view class'), # View All classes
    # path('deleteclass/<int:pk>', views.DeleteClass.as_view(), name='delete class'),
    path('editdelete/', views.EditDeleteClass.as_view()),  # updation view of a class
    path('deleteclass/<int:id>', views.DeleteClass),   # delete a class by its id
    path('updateclass/<int:pk>', views.UpdateClass.as_view(), name='update class'), # update a class by its id
    path('insertsubject/', views.InsertSubject.as_view(), name='add sub'), #Adding New Subject to class
    path('subjectlist/', views.SubjectList, name='all_subject'), # Show all subject list
    # --------------------------------------------------------


                # INSTITUTE info---------------->>>>>>>>>>>>>>>>>>>>>>>>>>>
    path('instituteinfo/', views.InstituteInfoView.as_view(), name='institute info'), #institute infomation CBV
    path('updateinstituteinfo/<int:pk>', views.UpdateInfo.as_view()),               #institute Information Updation
    path('insertinstituteinfo/', views.InsertInstituteInfo.as_view()),              #inserting New institute information
    # --------------------------------------------------------


                # STUDENT section------------>>>>>>>>>
    # path('addstudent/', views.AddStudent, name='add student'),
    path('viewallstudent/', views.AllStudent.as_view(), name='view student'),
    path('viewstudentdetail/<int:pk>', views.StudentDetailView.as_view()),
    path('addstudent/', views.AddStudent.as_view(), name='add student'),
    path('updatestudent/<int:pk>', views.UpdateStudent.as_view(), name='update_student'),
    path('deletestudent/<int:id>', views.DeleteStudent),
    path('admissionletterview/', views.AdmissionLetterView.as_view(), name='admission_letter_view'),
    path('admissionletter/<int:pk>', views.AdmissionLetter.as_view(), name='admission_letter'),

                    # EMPLOYEE section------------------>>>>>>>>
    path('viewallemployee/', views.AllEmp.as_view(), name='view_employee'),
    path('addemployee/', views.AddEmployee.as_view()),
    path('editviewemp/', views.EditDeleteEmployee.as_view()),
    path('viewemployeedetail/<int:pk>', views.EmployeeDetailView.as_view()),
    path('updateemployee/<int:pk>', views.UpdateEmployee.as_view()),
    path('deleteemployee/<int:id>', views.DeleteEmployee),

                    # SEARCH--------------------.>>>>>>>>>>>>>>>>>>>>>>>>>>>
    path('searchstudent/', views.SearchStudent), # Student search bar
    path('searchemp/', views.SearchEmployee),   # Employee search bar


                    # ACCOUNTS SECTION.-----------------.>>>>>>>>>>>>>>>>>>>>>>..
    # path('balance/', views.Balance.as_view(), name='balance'),
    path('balance/', views.Balance, name='balance'),
    path('addincome/', views.AddIncome.as_view(), name='add_income'),
    path('addexpense/', views.AddExpense.as_view(), name='add_expense'),

                # STUDENT ATTENDANCE------------------.>>>>>>>>>>>>>>>>>>
    path('allclassattendance/', views.AllClassAttendance, name='all_class_attendance_view'),
    path('studentattendance/<int:pk>', views.StudentAttendance, name='student_attendance'),
    path('employeeattendace/', views.EmployeeAttendance, name='employee_attendance'),
    path('studentattreport/', views.StudentAttedanceReport.as_view(), name='student_attendance_report'),
    path('employeeattreport/', views.EmployeeAttedanceReport.as_view(), name='employee_attendance_report'),

                    # Fees Section------------------------------------>>>>>>>>>>>>>
    path('feesclassview/', views.FeesClassView, name='fees_class_view'),
    path('feesstudentview/<int:pk>', views.FeesStudentView, name='fees_student_view'),
    path('getfeeslip/', views.FeeSearchReceipt),
    path('feelist/',views.ViewFeeStatus.as_view()),

    path('sendmail/<int:pk>',views.SendMail),
    path('feereceiptsearch/',views.FeeSearchReceipt),
    path('printfee/<int:pk>',views.PrintFee),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
