from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Users
# Create your views here.
def home(request):
    return render(request,"home.html")

@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data["email"]
        password = data["password"]
        try:
            u = Users.objects.get(email = email)
            if(password == u.password):
                print("login ok")
                return render(request,"home.html")
            else:
                print("worng pass")
        except Users.DoesNotExist:
            print("wrong email")

    return render(request,"login.html")
@csrf_exempt
def signup(request):
    if request.method == "POST":
        req = json.loads(request.body)
        if(req["action"]=="create_acc"):
            try:
                u = Users(
                    firstName = req["firstName"],
                    lastName = req["lastName"],
                    email = req["email"],
                    password = req["passwd"]
                )

                u.save()
                
                #return JsonResponse({
                #    "account_created":True,
                #})
                return render(request,"login.html")
            except Exception as e:
                return JsonResponse({
                    "account_created":False,
                }) 
    return render(request,"sign_up.html")