from django.shortcuts import render

# Create your views here.

def tweet_list(request):
    return render(request, "twitter/tweet_list.html")
