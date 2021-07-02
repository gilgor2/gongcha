# myproject/urls.py
"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from mydiary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('edit/<int:index>', views.edit, name='edit'),
    path('detail/<int:pk>/delete', views.delete, name="delete"),
    path('detail/<int:pk>/comment/<int:comment_pk>/delete/', views.delete_comment, name="delete_comment"),
    path('tagadd/<int:pk>',views.tag_add, name="tag_add"),
    path('tag', views.tag_home, name="tag_home"),
    path('hashtag/<int:pk>', views.tag_detail, name="tag_detail"),
    path('detail/<int:pk>/tag/<int:tag_pk>/delete', views.tag_delete, name="tag_delete"),
    path('search/', views.search, name="search"),
    path('like/<int:post_id>/', views.post_like_toggle, name="post_like_toggle"),
    path('login/',include('login.urls')),
    path('chat/', include('chat.urls')),
]
