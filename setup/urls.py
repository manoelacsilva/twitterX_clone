"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from twitter.views import TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView, like_tweet, singUp, signIn

urlpatterns = [
    path("admin/", admin.site.urls),
    path("feed", TweetListView.as_view(), name="tweet_list"),
    path("create", TweetCreateView.as_view(), name="tweet_create"),
    path("update/<int:pk>", TweetUpdateView.as_view(), name="tweet_update"),
    path("delete/<int:pk>", TweetDeleteView.as_view(), name="tweet_delete"),
    path("", singUp, name="sing_up"),
    path("signIn", signIn, name="sign_in"),
    path('like/<int:pk>/', like_tweet, name='like_tweet'),

]
