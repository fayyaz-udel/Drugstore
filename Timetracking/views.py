from datetime import datetime

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic

from .forms import LogForm
from .forms import NewUserForm
from .models import Log, User_ext


@login_required
def employee_dashboard(request):
    form = LogForm(request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
    else:
        initial = {'user': request.user}
        form = LogForm(initial=initial, user=request.user)

    return render(request, 'employee_dashboard_view.html',
                  {"form": form, "entries": Log.objects.all().filter(user=request.user)})


class LogList(generic.ListView):
    template_name = 'logs.html'
    context_object_name = 'entries'
    model = Log

@login_required
def log_delete_request(request, id):
    obj = get_object_or_404(Log, id=id, user=request.user)
    obj.delete()
    return redirect('/')

@login_required
def log_pay_request(request, id):
    obj = get_object_or_404(Log, id=id, user=request.user)
    if obj.paid is False:
        obj.paid = True
        obj.pay_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        obj.save()
    return redirect('/logs')

@login_required
def log_finish_request(request, id):
    obj = get_object_or_404(Log, id=id, user=request.user)
    if obj.finished is False:
        obj.finished = True
        obj.end_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        obj.save()
    return redirect('/')


@login_required
def log_create_request(request):
    if Log.objects.filter(finished=False, user=request.user).first() is None:
        Log(user=request.user, begin_dateTime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            end_dateTime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")).save()

    return redirect('/')


@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


class UserList(generic.ListView):
    template_name = 'user.html'
    context_object_name = 'entries'
    model = User_ext


@login_required
def user_delete_request(request, id):
    obj = get_object_or_404(User_ext, user_id=id)
    obj.delete()
    obj = get_object_or_404(User, id=id)
    obj.delete()
    return redirect('/user')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            User_ext(user=user).save()

            return redirect('/')

        else:
            return render(request=request,
                          template_name="register.html",
                          context={"form": form})

    form = NewUserForm
    return render(request=request,
                  template_name="register.html",
                  context={"form": form})
