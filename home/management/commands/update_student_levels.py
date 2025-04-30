# home/management/commands/update_student_levels.py
from django.core.management.base import BaseCommand
from home.models import AcademicSession

class Command(BaseCommand):
    help = 'Updates student levels based on academic session'

    def handle(self, *args, **kwargs):
        AcademicSession.update_student_levels()
        self.stdout.write(self.style.SUCCESS('Successfully updated student levels'))