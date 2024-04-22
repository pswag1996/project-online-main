from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .forms import * 
from collections import defaultdict


def index(request):
    context = {
        'test' : 'Hello',
    }

    return render(request,'index.html',context)

def login_view(request):
    print(request.POST)
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Pass",username,password)
                return HttpResponseRedirect('/main')
            else:
               return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def home(request):
    print(request)
    usernames = request.user.username

    context = {
        'username': usernames,
    }
    return render(request, 'main.html', context)

@login_required
def project_t(request):

    try :
        get_teacher = Teacher.objects.all()
        print(">>>>",get_teacher)
    except Exception as e :
        print(e)

    context = {
        'data' : get_teacher,
    }
    return render(request,'project_t.html',context)

@login_required
def project_y(request):
    projects = Project.objects.all()
    context = defaultdict(list)
  
    for project in projects:
        context[project.year].append(project)

    print(context)
    return render(request,'project_y.html',{'context': dict(context)})

@login_required
def project_s(request):
    project_data = Project.objects.filter(type='Software')
    print(project_data)
    context = {
        'data' : project_data,
    }
    return render(request,'project_s.html',context)

@login_required
def project_h(request):
    project_data = Project.objects.filter(type='Hardware')
    print(project_data)
    context = {
        'data' : project_data,
    }
    return render(request,'project_h.html',context)


@login_required
def profile(request):
    user_record = None
    usernames = request.user.username
    context = {}
    try:
        user_get = User.objects.get(username=usernames)  
        try :
            user_record = Teacher.objects.get(username=user_get) 
            context['role'] = 't' 
        except Exception as e:
            user_record = Student.objects.get(username=user_get)  
            context['role'] = 's'
    except ObjectDoesNotExist:
        pass
    print(context)
    context['user_record'] = user_record

    return render(request,'profile.html',context)
@login_required
def profile_save(request):
    user_record = None
    usernames = request.user.username
    context = {}
    q = request.POST

    try:
        user_get = User.objects.get(username=usernames)  
        try :
            user_record = Teacher.objects.get(username=user_get) 
            role = 't' 
        except Exception as e:
            user_record = Student.objects.get(username=user_get)  
            role = 's'
    except ObjectDoesNotExist:
        pass
    


    try:   
        if role == 't' :
            print(q)
            user_update = Teacher.objects.get(username=user_get)
            user_update.fullname = q.get('fullname')  
            user_update.id_teacher = q.get('id_teacher')   
            user_update.faculty = q.get('faculty')   
            user_update.branch = q.get('branch')      
            user_update.email = q.get('email')      
            user_update.phone = q.get('phone')        
            user_update.save() 
        elif role == 's' :
            print(q)
            user_update = Student.objects.get(username=user_get)
            user_update.fullname = q.get('fullname')  
            user_update.id_student = q.get('id_student')   
            user_update.faculty = q.get('faculty')   
            user_update.faculty = q.get('faculty')
            user_update.branch = q.get('branch')  
            user_update.year = q.get('year')        
            user_update.email = q.get('email')      
            user_update.phone = q.get('phone')        
            user_update.save() 
    except Exception as e :
         return JsonResponse({'error': 'error'})

    return JsonResponse({'status': 'success'})


def project_upload(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_field_name')  # Get the list of files
        if form.is_valid():
            project = form.save()  # Save the project first to get a project instance
            for f in files:
                File.objects.create(project=project, file=f, name=f.name)
            return redirect('some_view')
    else:
        form = ProjectForm()
    return render(request, 'your_template.html', {'form': form})


@login_required
def view_project(request):
    
    id = request.GET['id']
    projects = Project.objects.get(pk=id)
    print(projects)

    return render(request, 'view_project.html', {'projects': projects})

@login_required
def new_project(request):
    projects = ProjectForm


    return render(request, 'new_project.html', {'projects': projects})