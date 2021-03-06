from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(
        r'^login/$',
        auth_views.login,
        name = 'login',
        kwargs = {
            'template_name': 'accounts/login.html',
            'authentication_form': LoginForm,
        }
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        name = 'logout',
        kwargs = {
            'next_page': '/'
        }
    ),
    url(
        r'^password_change/$',
        auth_views.password_change,
        name = 'password_change',
        kwargs = {
            'template_name': 'accounts/password_change_form.html',
            'post_change_redirect': 'accounts:password_change_success',
        }
    ),
    url(
        r'^password_change_success/$',
        auth_views.password_change_done,
        name = 'password_change_success',
        kwargs = {
            'template_name': 'accounts/password_change_success.html'
        }
    ),
    url(r'^register/$', views.register, name='register'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    url(r'^(?P<profile_username>[-\w]+)/$', views.peer_profile, name='profile_view')
]
