from celery import shared_task
from django.utils import timezone
from .models import Student, Semester, Department
from datetime import datetime

@shared_task
def update_student_levels():
    current_semester = Semester.get_current()
    if not current_semester:
        return
    
    # Only update levels after second semester ends
    if current_semester.name == 'Second':
        today = timezone.now().date()
        
        # Check if we're at the end of second semester
        if today >= current_semester.end_date:
            students = Student.objects.filter(status='Active')
            
            for student in students:
                department = student.department
                max_level = department.max_level
                
                # Check if student should graduate
                if student.level >= max_level:
                    student.status = 'Graduated'
                else:
                    student.level += 100
                
                student.last_level_update = today
                student.save()

@shared_task
def update_current_semester():
    today = timezone.now().date()
    
    # Get all semesters
    semesters = Semester.objects.all()
    
    for semester in semesters:
        if semester.start_date <= today <= semester.end_date:
            semester.is_current = True
            semester.save()
            break

@shared_task
def mark_absent_students():
    # Import here to avoid circular imports
    from .models import Attendance, Course
    # Add your absent marking logic here
    pass