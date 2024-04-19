from django.contrib import admin

# Register your models here.
from .models import Professor
from .models import CourseSection
from .models import Department
from .models import Research

admin.site.register(Professor)
admin.site.register(CourseSection)
admin.site.register(Department)
admin.site.register(Research)
