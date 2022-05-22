import json

import requests

from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Films, Genres, Comment
from django.core.paginator import Paginator
from .forms import CommentForm


# Create your views here.
# Начал 14 мая
# 15 мая сделал простенький дизайн с помощью bootstrap, сделал базовые вещи модели и тд., сделал поиск по сайту, настроил админку немного и тд.
# 16 мая пропустил день полностью, пришлось делать проект на Java для экзамена по программированию
# 17 мая немного разобрался с тестами, написал тесты для url и views,
# 17 мая добавил форму для комментариев, которая привязана к конкретному фильму, подключил капчу
# 18 мая реализовал авторизацию с восстановлением почты и тд и тп.
# 19 мая - 21 мая не было времени просто делал задачки с leetcode
# Этот проект пока буду заканчивать впереди сессия, не реализовал только рейтинг, тк простой рейтинг делать нету смысла, а делать сложную систему рейтинга я пока не готов


# Закончил 22 мая


def base(request):
    search = request.GET.get('sear', '')
    if search:
        film = Films.objects.filter(title__icontains=search)
    else:
        film = Films.objects.all()


    cat = Genres.objects.all()
    pag = Paginator(film, 9)
    page_number = request.GET.get('page')
    pag = pag.get_page(page_number)

    return render(request, 'main/base.html', {'pag': pag, 'cat': cat})


def genr(request, genr):
    sl = get_object_or_404(Genres, slug=genr)
    film = Films.objects.filter(genre=sl.id)
    cat = Genres.objects.all()
    pag = Paginator(film, 9)
    page_number = request.GET.get('page')
    pag = pag.get_page(page_number)

    return render(request, 'main/genr.html', {'sl': sl, 'pag': pag, 'film': film, 'cat': cat})



def film_watch(request, filmm):                       #Как нормально разберусь с тестами, не забыть разобратся с Ajax(немного)
    ml = get_object_or_404(Films, id=filmm)
    post = get_object_or_404(Films, id=ml.id)


    if request.method == 'POST':
        form = CommentForm(request.POST)
        captcha_token = request.POST.get("g-recaptcha-response")
        cap_url = "https://www.google.com/recaptcha/api/siteverify"
        cap_secret = "6LcIoPgfAAAAAF7cL2FSmnhCCvcdg5WkHT-ZQWU6"
        cap_data = {"secret": cap_secret, "response": captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)             # ЭТО ВСЁ КАПЧА
        cap_json = json.loads(cap_server_response.text)
        if cap_json['success']==False:

            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


        if form.is_valid():

            comm = form.save(commit=False)
            comm.user = request.user
            comm.post = post
            comm.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        form = CommentForm


    post_comments = Comment.objects.all().filter(post=ml.pk)



    return render(request, 'main/film_watch.html', {'ml': ml, 'form': form, 'post_comments': post_comments})



def email_success(request):
    res = 'Email is verified!'
    return HttpResponse('<p>%s</p>' % res)