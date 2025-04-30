from django.core.management.base import BaseCommand
from django.utils import timezone
from home.models import Semester
from datetime import date

class Command(BaseCommand):
    help = 'Setup initial semesters with correct dates'

    def handle(self, *args, **kwargs):
        try:
            # Create First Semester
            first_sem, created = Semester.objects.get_or_create(
                name='First',
                defaults={
                    'start_date': date(2024, 9, 1),
                    'end_date': date(2024, 12, 31),
                    'is_current': False
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(self.style.SUCCESS(f'First Semester: {status}'))

            # Create Second Semester
            second_sem, created = Semester.objects.get_or_create(
                name='Second',
                defaults={
                    'start_date': date(2025, 1, 1),
                    'end_date': date(2025, 4, 30),
                    'is_current': False
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(self.style.SUCCESS(f'Second Semester: {status}'))

            # Create Summer Semester
            summer_sem, created = Semester.objects.get_or_create(
                name='Summer',
                defaults={
                    'start_date': date(2025, 6, 1),
                    'end_date': date(2025, 8, 31),
                    'is_current': False
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(self.style.SUCCESS(f'Summer Semester: {status}'))

            # Set current semester based on today's date
            today = timezone.now().date()
            current_set = False

            for semester in Semester.objects.all():
                if semester.start_date <= today <= semester.end_date:
                    semester.is_current = True
                    semester.save()
                    current_set = True
                    self.stdout.write(
                        self.style.SUCCESS(f'Set current semester to: {semester.name}')
                    )

            if not current_set:
                self.stdout.write(
                    self.style.WARNING('No current semester set for today\'s date')
                )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))