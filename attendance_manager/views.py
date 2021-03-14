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


from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'attendance_manager.hello'    # a unique code

    def do(self):
        print('hello ')    # do your thing here