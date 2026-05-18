from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_list_or_404
from .forms import CreateNewTask, CreateNewProject
# Create your views here.

def index(request):
    title = "Bienvenido a Django"
    return render(request,'index.html',{
        'title': title
    })

def hello(request, username):
    print(type(username))
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    username = 'Fbi4n'
    return render(request,'about/about.html',{
        'username': username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

def create_project(request):
    if request.method == 'GET':
        # mostrar interfaz
         return render(request, 'projects/create_project.html',{
         'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    

def task(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request,'tasks/task.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        # mostrar interfaz
         return render(request, 'tasks/create_task.html',{
         'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], 
        description=request.POST['description'], project_id=1)
        return redirect('task')

def project_detail(request, id):
    project = Project.objects.get(id=id)
    tasks = Task.objects.filter(project_id=id)
    get_list_or_404(Project, id=id)
    print(project)
    return render(request, 'projects/detail.html',{
        'project': project,
        'tasks': tasks

    })