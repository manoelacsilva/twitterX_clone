from django import forms
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from twitter.forms import SignInForm, SignUpForm
from .models import Tweet
from django.contrib.auth.models import User

class TweetListView(ListView):
    model = Tweet

    def listTweets(request):
        model = Tweet
        user = User.objects.get(id=request.user.id)
        return render(request, "twitter/singup.html", {"tweets": model, "user": user})
    # def home(request):
    #     if request.user.is_authenticated:
    #         return redirect("tweet_list")

    #     return render(request, "twitter/singup.html")

class TweetCreateView(CreateView):
    model = Tweet
    fields = ["title"]
    success_url = reverse_lazy("tweet_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TweetUpdateView(UpdateView):
    model = Tweet
    fields = ["title"]
    success_url = reverse_lazy("tweet_list")

class TweetDeleteView(DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet_list")

def singUp(request):
    if request.method == "POST": 
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["usuario"]
            first_name = form.cleaned_data["nome"].lower()
            last_name = form.cleaned_data["sobrenome"].lower()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["senha"]

            double_user = User.objects.filter(username=username).first()

            if double_user:
                return HttpResponse("The username already exists.")
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("tweet_list")
        else:
            return HttpResponse("Something went wrong. Try again later.")
    else:
        form = SignUpForm()
        return render(request, "twitter/singup.html", {"form": form})

def signIn(request):
    form = SignInForm()
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["usuario"].lower()
            password = form.cleaned_data["senha"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("tweet_list")

        return HttpResponse("Check out your informations.")

    return render(request, "twitter/signin.html", {"form": form})

def like_tweet(request, pk):
    if request.user.is_authenticated:
        tweet = get_object_or_404(Tweet, id=pk)

        if tweet.likes.filter(id=request.user.id):
            tweet.likes.remove(request.user)
        else:
            tweet.likes.add(request.user)

        return redirect(request.META.get("HTTP_REFERER"))

    return redirect("")