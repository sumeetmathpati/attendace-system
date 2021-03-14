from django.shortcuts import render


def index(request):
    context = {
    }
    return render(request, 'attendance_manager/index.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'attendance_manager/about.html', context)

