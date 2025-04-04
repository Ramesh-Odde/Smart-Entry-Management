from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})


def student(request):
    return render(request, 'student.html', {})

def faculty(request):
    return render(request, 'faculty.html', {})

def guest(request):
    return render(request, 'guest.html', {})
