from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User

BRANCH_CHOICES = [
    ('Computer', 'Computer'),
    ('Electronic', 'Electronic'),
    ('Mechatronic', 'Mechatronic'),
    ('Electrical', 'Electrical'),
]

FACULTY_CHOICES = [
    ('Engineering' , 'Engineering'),
    ('Science' , 'Science'),
    ('Education' , 'Education'),
    ('Accountancy' , 'Accountancy')
]

TYPE_CHOICES =[
    ('Hardware' , 'Hardware'),
    ('Software' , 'Software'),
]

YEAR_CHOICES =[
    ('2563' , '2562'),
    ('2564' , '2564'),
    ('2565' , '2565'),
    ('2566' , '2566'),
    ('2567' , '2567'),
    ('2568' , '2568'),
]

# TAG_CHOICES =[
#     ('ARDUINO' , 'ARDUINO'),
#     ('CSS' , 'CSS'),
#     ('HTML' , 'HTML'),
#     ('JAVA' , 'JAVA'),
#     ('JAVASCRIPT' , 'JAVASCRIPT'),
#     ('PYTHON' , 'PYTHON'),
#     ('C#' , 'C#'),
#     ('C++' , 'C++'),
#     ('C' , 'C'),
#     ('Bootstrap' , 'Bootstrap'),
#     ('TailwindCSS' , 'TailwindCSS'),
#     ('C' , 'C'),
#     ('C' , 'C'),
# ]
class Teacher(models.Model):
    id_teacher = models.IntegerField()
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Teacher')
    fullname = models.CharField(null=False,max_length=255)
    faculty = models.CharField(choices=FACULTY_CHOICES,null=True,max_length=255)
    branch = models.CharField(choices=BRANCH_CHOICES,null=True, max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    img = models.ImageField(upload_to='img/', height_field=None, width_field=None, max_length=None)
    def __str__(self): 
         return self.fullname


class Student(models.Model):
    id_student = models.IntegerField()
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Student')
    # password = models.CharField(max_length=255,null=False)
    fullname = models.CharField(null=False,max_length=255)
    faculty = models.CharField(choices=FACULTY_CHOICES,null=True,max_length=255)
    branch = models.CharField(choices=BRANCH_CHOICES,null=True, max_length=255)
    email = models.EmailField(max_length=254)
    year = models.IntegerField()
    phone = models.IntegerField()
    img= models.ImageField(upload_to='img/', height_field=None, width_field=None, max_length=None)
    
    def __str__(self): 
         return self.fullname

class Project(models.Model):
    id_project = models.IntegerField()
    id_student = models.ForeignKey(Student, verbose_name="id_student", on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(Teacher, verbose_name="id_teacher", on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=255)
    type = models.CharField(choices=TYPE_CHOICES,null=False, max_length=255)
    year = models.CharField(choices=YEAR_CHOICES,null=False, max_length=255)
    tag = models.TextField(null=True,blank=True)
    
    
    def __str__(self): 
         return self.name
    
class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')  
    project = models.ForeignKey(Project, verbose_name="id_project", on_delete=models.CASCADE, related_name='project_files')
    def __str__(self): 
        return self.name
