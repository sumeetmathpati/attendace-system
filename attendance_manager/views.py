from django.shortcuts import render, redirect
from .forms import TakeAttendance
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def index(request):
    context = {}
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = TakeAttendance(request.POST)
            if form.is_valid():
                email = request.user.email
                class_name = form.cleaned_data.get('class_name')
                # messages.success(request, f'Account has been created, you can log in.')
                print(f'{class_name}, {email}')
                return redirect('index')
    else:
        if request.user.is_authenticated:
            form = TakeAttendance()
            context['form'] = form
   
    return render(request, 'attendance_manager/index.html', context)


@csrf_exempt
def mark_attendance(request):
    if request.method == 'POST':
        print(f"************{request.POST.get('id')}")
    else:
        print('*************')
    print(get_client_ip(request))
    return HttpResponse(status=200)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip