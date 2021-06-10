import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm, CreateImgNewsForm, UserRegisterForm, CreateVideoForm
from gamenews.service import group_required


def startpage(request):
    context = {}
    context.update({'news': News.objects.order_by('-date')[:2],
                    'videos': Videos.objects.order_by('-date')[:2]})
    return render(request, 'startpage.html', context)


def newspage(request):
    context = {}
    context.update({'news': News.objects.order_by('-date')})
    return render(request, 'newspage.html', context)


def curr_news_page(request, new):
    context = {}
    context.update({'news': News.objects.get(id=new)})
    context.update({'comms': News.objects.get(id=new).comments.order_by('-id')})
    return render(request, 'currnewspage.html', context)


@login_required
def add_comm(request):
    if request.POST:
        comment_text = request.POST.get('comment_text')
        newsid = request.POST.get('newsid')
        news = News.objects.get(id=newsid)
        user = User.objects.get(id=request.user.id)
        new_comment = Comment.objects.create(author=user,
                                             text=comment_text)
        new_comment.save()
        news.comments.add(new_comment)
        data_response = {'success': True,
                         'comment_text': comment_text,
                         'comm_id': new_comment.id}

        return HttpResponse(json.dumps(data_response), content_type='application/json')


@group_required('moder')
def del_comm(request):
    if request.POST:
        comment_id = request.POST.get('comm_id')
        comm = Comment.objects.get(id=comment_id)
        comm.delete()
        data_response = {'success': True}

        return HttpResponse(json.dumps(data_response), content_type='application/json')


def contactpage(request):
    form = ContactForm()
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}

    return render(request, 'contactpage.html', context)


@group_required('redactor')
def create_news(request):
    context = {}
    if request.POST:
        new_news = News.objects.create(text=request.POST.get('text'),
                                       title=request.POST.get('title'),
                                       author=request.user)
        new_news.save()
        form_img = CreateImgNewsForm(request.POST, request.FILES, instance=new_news)
        if form_img.is_valid():
            form_img.save()
        context = {'good': True}
    return render(request, 'create-news.html', context)


def logout_user(request):
    logout(request)
    return redirect('startpage')


def register_user(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    return render(request, 'register-page.html')


def login_user(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('startpage')
    else:
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect('startpage')
    return render(request, 'login-page.html')


@login_required
def add_comm_video(request):
    if request.POST:
        comment_text = request.POST.get('comment_text')
        newsid = request.POST.get('newsid')
        news = Videos.objects.get(id=newsid)
        user = User.objects.get(id=request.user.id)
        new_comment = Comment.objects.create(author=user,
                                             text=comment_text)
        new_comment.save()
        news.comments.add(new_comment)
        data_response = {'success': True,
                         'comment_text': comment_text,
                         'comm_id': new_comment.id}

        return HttpResponse(json.dumps(data_response), content_type='application/json')


@group_required('moder')
def del_comm_video(request):
    if request.POST:
        comment_id = request.POST.get('comm_id')
        comm = Comment.objects.get(id=comment_id)
        comm.delete()
        data_response = {'success': True}

        return HttpResponse(json.dumps(data_response), content_type='application/json')


def all_videos(request):
    context = {}
    videos = Videos.objects.order_by('-date')
    context.update({'videos': videos})

    return render(request, 'videospage.html', context)


def curr_video(request, videoid):
    context = {}
    context.update({'video': Videos.objects.get(id=videoid),
                    'comms': Videos.objects.get(id=videoid).comments.order_by('-id')})

    return render(request, 'currvideopage.html', context)


def search_page(request):
    context = {}
    search_text = request.GET.get('stext')
    news = News.objects.filter(title__icontains=search_text)
    videos = Videos.objects.filter(title__icontains=search_text)

    context.update({'news': news,
                    'videos': videos})

    return render(request, 'searchpage.html', context)


@login_required(redirect_field_name='login_user')
def feedback_page(request):
    context = {}
    if request.POST:
        theme = request.POST.get('theme')
        text = request.POST.get('text')
        user = request.user
        new_feedback = FeedBack.objects.create(theme=theme,
                                               text=text,
                                               user=user)
        new_feedback.save()
        context.update({'good': True})

    return render(request, 'feedbackpage.html', context)


@group_required('redactor')
def create_videos(request):
    context = {}
    if request.POST:
        new_news = Videos.objects.create(title=request.POST.get('title'),
                                         author=request.user)
        new_news.save()
        form_video = CreateVideoForm(request.POST, request.FILES, instance=new_news)
        if form_video.is_valid():
            form_video.save()
        context = {'good': True}
    return render(request, 'create-video.html', context)
