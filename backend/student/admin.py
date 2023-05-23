from django.contrib import admin
from student.models import Student
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    # list_fields =  ('name')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Student,MemberAdmin)



