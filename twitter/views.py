from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tweet
from django.contrib.auth.models import User

class TweetListView(ListView):
    model = Tweet

class TweetCreateView(CreateView):
    model = Tweet
    fields = ["title", "deadline"]
    success_url = reverse_lazy("tweet_list")

class TweetUpdateView(UpdateView):
    model = Tweet
    fields = ["title", "deadline"]
    success_url = reverse_lazy("tweet_list")

class TweetDeleteView(DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet_list")

def singUp(request):
    if request.method == "POST": return HttpResponse("Formulário enviado com sucesso")
    else: return render(request, "singup.html")