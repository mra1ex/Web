from django.shortcuts import render, redirect
from .models import People, Like
from .forms import PeopleForm, LikeForm
import hashlib
import re

from django.http import JsonResponse
import requests
import json


def general(request):

    try: likes = Like.objects.all()
    except: likes = []
    data = { 'like_amount': len(likes) }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            like = form.save()

    try: likes = Like.objects.all()
    except: likes = []
    data = { 'like_amount': len(likes), 'form': LikeForm()}

    return render(request, 'main/general.html', data)


def signup(request):
    mail_error = ''
    password_error = ''
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            mail = request.POST.get("mail")
            password = request.POST.get("password")
            error = False
            if '@' and ('.ru' or '.com') in mail is None:
                mail_error = 'Почта должна быть действительной'
                error = True
            if len(password) > 20 or len(password) < 8 or re.match(
                    r'(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,20}', password) is None:
                password_error = "Пароль должен содержать от 8 до 20 символов, хотя бы одно число, " \
                                 "буквы верхнего/нижнего регистра и спецсимвол !@#$%^&*`) "
                error = True
            people = People.objects.all()
            for i in people:
                if i.mail == mail:
                    mail_error = "Такая почта занята"
                    error = True
            if not error:
                f = People(
                    name=request.POST.get("name"),
                    surname=request.POST.get("surname"),
                    mail=request.POST.get("mail"),
                    # password=request.POST.get("password"),
                    password=hashlib.sha1(request.POST.get("password").encode('utf-8')).hexdigest()
                )
                f.save()
                send_info(mail)
                return redirect('general')
    else:
        form = PeopleForm()

    data = {
        'form': form,
        'mail_error': mail_error,
        'password_error': password_error,
    }
    return render(request, 'main/signup.html', data)


def signin(request):
    mail_error = ''
    password_error = ''
    if request.method == "POST":
        form = PeopleForm(request.POST)
        print('-------------')
        # if form.is_valid():
        mail = request.POST.get("mail")
        password = request.POST.get("password")
        error = False
        if '@' and ('.ru' or '.com') in mail is None:
            mail_error = 'Почта должна быть действительной'
            error = True
        if len(password) > 20 or len(password) < 8 or re.match(r'(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,20}', password) is None:
            password_error = "Пароль должен содержать от 8 до 20 символов, хотя бы одно число, " \
                             "буквы верхнего/нижнего регистра и спецсимвол !@#$%^&*`) "
            error = True


        if not error:
            people = People.objects.all()
            for i in people:
                if i.mail == mail:
                    if i.password == hashlib.sha1(request.POST.get("password").encode('utf-8')).hexdigest():
                        return redirect('general')
                    break
                password_error = "Неправильные почта или пароль"
    else:
        form = PeopleForm

    data = {
        'form': form,
        'mail_error': mail_error,
        'password_error': password_error
    }

    return render(request, 'main/signin.html', data)


def general1(request):
    return render(request, 'main/general1.html')


def send_info(nickname):
    TOKEN = "6169854972:AAGAWl3x042IeXdTxVPVVc9xNFI_F0CwQfo"
    chat_id = "-1001883911240"
    message = f"Заявка с сайта!\nИмя пользователя: {nickname}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()




# def create(request):
#     error = ''
#     if request.method == "POST":
#         form = PeoplesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('general')
#         else:
#             error = 'Форма была неверной'
#     form = PeoplesForm
#
#     data = {
#         'form': form,
#         'error': error
#     }
#
#     return render(request, 'main/create.html', data)
#
