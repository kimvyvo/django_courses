from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    if not request.session:
        request.session['name'] = ''
        request.session['desc'] = ''
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request, methods=['POST']):
    request.session['name'] = request.POST['name']
    request.session['desc'] = request.POST['desc']
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        messages.success(request, "Course successfully added.")
        request.session['name'] = ''
        request.session['desc'] = ''
    return redirect('/')

def remove(request, id):
    context = {
        'course' : Course.objects.get(id=id)
    }
    return render(request, 'courses/remove.html', context)

def destroy(request, id, method=['POST']):
    Course.objects.get(id=id).delete()
    return redirect('/')
