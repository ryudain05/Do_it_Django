"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pybo import views
from common import account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('question/create/', views.question_create, name='question_create'),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path

    # url을 네임스페이스가 없는 앱, 혹은 mysite\config\urls.py의 urlpatterns 리스트 원소로 추가한다.
    # => 기존은 네임스페이스가 없는 URL로 연결시키기 때문
    path('reset/<uidb64>/<token>/', account_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]