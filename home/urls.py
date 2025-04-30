from django.shortcuts import render
from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view


from django.conf import settings
from django.conf.urls.static import static
from .views import add_lecturer

from django.contrib.auth.decorators import login_required


# Define urlpatterns before using it
urlpatterns = [
    path('add_lecturer/', add_lecturer, name='add_lecturer'),
]

from django.urls import path
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect


# Append static URLs if in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

def is_lecturer(user):
    return user.is_authenticated and user.role == 'lecturer'

def is_student(user):
    return user.is_authenticated and user.role == 'student'

admin_dashboard_view = login_required(user_passes_test(is_admin, login_url='index')(lambda request: render(request, 'home/admin_dashboard.html')))
student_panel_view = login_required(user_passes_test(is_student, login_url='index')(lambda request: render(request, 'home/student-panel.html')))
lecturer_panel_view = login_required(user_passes_test(is_lecturer, login_url='index')(lambda request: render(request, 'home/lecturer-panel.html')))


urlpatterns = [
    path('', views.index, name='index'), 

    path('home/admin/messages/', views.admin_messages, name='admin_messages'),
    path('get-unread-messages-count/', views.get_unread_messages_count, name='get_unread_messages_count'),

    path('get-message/<int:message_id>/', views.get_message, name='get_message'),
    path('toggle-message-status/<int:message_id>/', views.toggle_message_status, name='toggle_message_status'),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('mark-all-messages-read/', views.mark_all_messages_read, name='mark_all_messages_read'),

    # path('login/', views.login, name='login'),
    path('login/', views.login_view, name='login'),
    path('home/admin_dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('home/student/', student_panel_view, name='student_panel'),
    path('home/lecturer/', lecturer_panel_view, name='lecturer_panel'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('get_attendance_data/', views.get_attendance_data, name='get_attendance_data'),
    path('export_excel/', views.export_excel, name='export_excel'),
    path('get_attendance_summary/', views.get_attendance_summary, name='get_attendance_summary'),
    path('export_summary_pdf/', views.export_summary_pdf, name='export_summary_pdf'),
    path('get-dashboard-stats/', views.get_dashboard_stats, name='get_dashboard_stats'),


    path('fingerprint/', views.fingerprint, name='fingerprint'),
    path('verify/', views.verify, name='verify'),
    path('mark/', views.mark, name='mark'),
    path('get-courses/', views.get_courses, name='get_courses'),
    path('home/admin/report/', views.report, name='report'),
    path('home/admin/settings/', views.settings, name='settings'),
    path('home/admin/add_course/', views.course, name='course'),
    path('home/admin/summary/', views.admin_summary, name='admin_summary'),
    path('home/admin/add_student/', views.add_student, name='add_student'),
    path('home/admin/add_lecturer/', views.add_lecturer, name='add_lecturer'),
    path('home/admin/manage_lecturer/', views.modify_lecturer, name='modify_lecturer'),

    path('home/student/course_list/<int:student_id>/', views.student_courses, name='student_courses'),
    
    path('settings/delete_session/<int:pk>/', views.delete_session, name='delete_session'),
    path('settings/delete_semester/<int:pk>/', views.delete_semester, name='delete_semester'),
    path('settings/delete_department/<int:pk>/', views.delete_department, name='delete_department'),
    
    path('delete_lecturer/<int:lecturer_id>/', views.delete_lecturer, name='delete_lecturer'),
    path('home/admin/modify_lecturer/<str:lecturer_id>/', views.modify_lecturer_page, name='modify_lecturer_page'),

    path('home/admin/manage_courses/', views.modify_course, name='modify_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('home/admin/modify_course/<int:course_id>/', views.modify_course_page, name='modify_course_page'),
    path('home/admin/manage_students/', views.modify_student, name='modify_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('home/admin/modify_student/<int:student_id>/', views.modify_student_page, name='modify_student_page'),
    path('export_student_attendance_excel/', views.export_student_attendance_excel, name='export_student_attendance_excel'),
    path('get_student_attendance_data/', views.get_student_attendance_data, name='get_student_attendance_data'),
    
    path('get_student_summary_data/', views.get_student_summary_data, name='get_student_summary_data'),
    path('timetable/', views.generate_timetable_pdf, name='generate_timetable'),
    path('export_student_summary_pdf/', views.export_student_summary_pdf, name='export_student_summary_pdf'),

    path('home/lecturer/report/', views.lecturer_report, name='lecturer_report'),
    path('get_lecturer_attendance_data/', views.get_lecturer_attendance_data, name='get_lecturer_attendance_data'),
    path('export_lecturer_attendance/', views.export_lecturer_attendance, name='export_lecturer_attendance'),
    
    path('home/lecturer/summary/', views.lecturer_summary, name='lecturer_summary'),
    path('get_lecturer_summary_data/', views.get_lecturer_summary_data, name='get_lecturer_summary_data'),
    path('export_lecturer_summary_pdf/', views.export_lecturer_summary_pdf, name='export_lecturer_summary_pdf'),
    path('home/lecturer/profile/', views.profile, name='profile'),
    path('home/lecturer/manage_class/', views.manage_class, name='manage_class'),
    path('home/lecturer/modify_class/<int:course_id>/', views.modify_class, name='modify_class'),
    path('home/lecturer/modify_profile/', views.modify_profile, name='modify_profile'),
    path('home/student/report/', views.student_report, name='student_report'),
    path('home/student/summary/', views.student_summary, name='student_summary'),
    path('home/student/modify_profile/', views.student_modify, name='student_modify'),
    path('home/student/profile/', views.student_profile, name='student_profile'),
    path('home/admin/view_student_courses/<int:student_id>/', views.view_student_courses, name='view_student_courses'),
    path('assign_courses/', views.assign_courses_to_student, name='assign_courses_to_student'),
    path('remove_student_course/<int:student_id>/<int:course_id>/', views.remove_student_course, name='remove_student_course'),
    path('api/lecturer-stats/', views.get_lecturer_stats, name='lecturer-stats'),
    path('api/student-stats/', views.get_student_stats, name='student-stats'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)