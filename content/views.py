from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all() # select * from content_feed;
        for feed in feed_list:
            print(feed.content)
        return render(request, "kimstagram/main.html", context=dict(feeds=feed_list))