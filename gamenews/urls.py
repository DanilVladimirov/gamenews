from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from gamenews import settings
from newsapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', startpage, name='startpage'),
    path('news/', newspage, name='newspage'),
    path('add_comm/', add_comm, name='add_comm'),
    path('news/<int:new>/', curr_news_page, name='currnews'),
    path('contact/', contactpage, name='contact'),
    path('del_comm/', del_comm, name='del_comm'),
    path('create-news/', create_news, name='create_news'),
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('add_comm_video/', add_comm_video, name='add_comm_video'),
    path('del_comm_video/', del_comm_video, name='del_comm_video'),
    path('videos/', all_videos, name='videos'),
    path('video/<int:videoid>/', curr_video, name='video'),
    path('search/', search_page, name='search_page'),
    path('feedback/', feedback_page, name='feedback_page'),
    path('create_video/', create_videos, name='create_video')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
