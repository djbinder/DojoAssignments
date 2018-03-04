from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
from django.contrib import messages
from datetime import datetime, date, timedelta
from django.views.generic.dates import TodayArchiveView
# from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth import authenticate
# from django.contrib.auth import views as auth_views


#INDEX WELCOME PAGE
def index(request):
    if "userid" in request.session:  
        return redirect('/show')
    else:                           
        return render(request, 'beltapp/index.html') 

def createuser(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        hashmasterflash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()) 
        newuser = User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=hashmasterflash,
            birth_date=request.POST['birth_date'],
            )
        request.session['userid'] = newuser.id
        request.session['name'] = newuser.name
        return render(request, 'beltapp/appointments.html')

def login(request):
    errors = User.objects.loginvalidate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.filter(email=request.POST['email'])[0]
        request.session['userid'] = user.id
        request.session['name'] = user.name
        return redirect('/show')

def show(request):
    print "WE ARE SHOWING HERE"
    userid=request.session['userid']
    today = date.today()
    tomorrow = date.today() + timedelta(1)
    # print today
    # print userid
    print tomorrow
    context = {
        'today': today,
        'appointmentstoday': Appointment.objects.filter(date=today, userid=userid).order_by('time'),
        'appointmentsfuture': Appointment.objects.filter(date__gte=tomorrow, userid=userid).order_by('date')
    }
    return render(request, 'beltapp/appointments.html', context)

def createappointment(request):
    errors = Appointment.objects.appointmentvalidate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/show')
    else:
        # user = User.objects.filter(id=request.session['userid'])
        # print user
        userid=request.session['userid']
        print userid
        newapppointment = Appointment.objects.create(
            task=request.POST['task'],
            date=request.POST['date'],
            time=request.POST['time'],
            status="Pending",
            userid=userid
        )
    return redirect('/show')

def edit(request, id):
    print "WE ARE EDITING HERE"
    appointment_list = Appointment.objects.filter(id=id)
    print "PRINT APPOINTMENT LIST"
    print appointment_list
    if len(appointment_list) > 0:
        appointment = appointment_list[0]
        print appointment
        timeget = appointment.time
        print timeget
        time = timeget.strftime('%I:%M %p')
        print time
        appt_id_get = appointment.id
        print appt_id_get
        print appointment.status
        context = {
            "task": appointment.task,
            "status": appointment.status,
            "date": appointment.date,
            "time": appointment.time,
            "id": appt_id_get,
        }
        print id
        return render(request, "beltapp/edit.html", context)
    else:
        return render(request, 'appointments.html')

def update(request, id):
    appointment_list = Appointment.objects.filter(id=id)
    if len(appointment_list) > 0:
        appointment = appointment_list[0]
        errors = Appointment.objects.appointmentvalidate(request.POST)
        print appointment
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/edit/'+id)
        else:
            print appointment.id
            appointment.task = request.POST['task']
            appointment.status = request.POST['status']
            appointment.date = request.POST['date']
            appointment.time = request.POST['time']
            appointment.save(update_fields=['task', 'status', 'date', 'time'])
            return redirect('/show')
    else:
        pass

def destroy(request, id):
    appointment = Appointment.objects.filter(id=id)
    appointment.delete()
    return redirect('/')

def delete(request, id):
    appointment_list = Appointment.objects.filter(id=id)
    print appointment_list
    if len(appointment_list) > 0:
        appointment = appointment_list[0]
        task = appointment.task
        id = appointment.id
        context = {
            'task': task,
            'id': id, 
        }
    return render(request, 'beltapp/delete.html', context)

def logout(request, methods='POST'):
    request.session.clear() 
    return redirect('/')

# def success(request):
#     user = request.session['userid']
#     return render(request, 'beltapp/appointments.html')






    # appointment_list = Appointment.objects.filter(id=id)
    # print "PRINT APPOINTMENT LIST"
    # print appointment_list
    # appointment = appointment_list[0]
    # print "PRINT APPOINTMENT"
    # print appointment
    # print "PRINT TIME"
    # time = appointment.time
    # print time
    # print "APPOINTMENT.TIME"
    # print appointment.time
    # task=request.POST['task'],
    # print task,
    # print request.POST['task'],
    # date=request.POST['date'],
    # print date,
    # time=request.POST['time'],
    # print time,
    # appointment.status=request.POST['status'],
    # print appointment.status,
    # print request.POST['status'],
    # context = {
    #     'id': Appointment.objects.get(id=id)
    # }
    # print id
    # return render(request, 'beltapp/edit.html', context)



    # def update(request):
    # print "WE ARE UPDATING HERE"
    # appointment = Appointment.objects.filter(id=id)
    # # id = appointment.id
    # # print id
    # # id = appointment.id
    # print appointment
    # print appointment.task
    # print appointment
    # # task_update = request.GET['task']
    # # appointment.task = task_update
    # # appointment.save(update_fields=['task'])
    # return redirect('/')


    # def showedit(request, id):
#     userid=request.session['userid']
#     appointment_list = Appointment.objects.filter(id=id)
#     print appointment_list
#     if len(appointment_list) > 0:
#         appointment = appointment_list[0]
#         print appointment
#         timeget = appointment.time
#         print timeget
#         time = timeget.strftime('%I:%M %p')
#         print time
#         appt_id_get = appointment.id
#         print appt_id_get
#         context = {
#             "task": appointment.task,
#             "status": appointment.status,
#             "date": appointment.date,
#             "time": time
#         }
#         return render(request, 'beltapp/edit.html', context)
#     else:
#         return render(request, 'appointments.html')