from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("겟호출")
        return render(request, "kimstagram/main.html")

    def post(self, request):
        print("포스트호출")
        return render(request, "kimstagram/main.html")