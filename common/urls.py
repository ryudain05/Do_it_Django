from django.urls import path
from django.contrib.auth import views as auth_views
from . import account_views

app_name = 'common'


urlpatterns = [
    # 로그인, 로그아웃, 회원가입
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', account_views.signup, name='signup'),

    # 비밀번호 변경
    path('password_reset/', account_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', account_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
]