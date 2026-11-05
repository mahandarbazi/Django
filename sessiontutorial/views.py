from django.shortcuts import render,HttpResponse
from django.http import HttpRequest


def set_session(request:HttpRequest):
    request.session["username"] = "MahanDarbazi"
    return HttpResponse("session seted")

def get_session(request:HttpRequest):
    username = request.session.get("username","mahan")
    return HttpResponse(f"your username is:{username}")

def update_session(request:HttpRequest):
    request.session["username"] = "Mahan"
    return HttpResponse("session updated")

def delete_session(request:HttpRequest):
    del request.session["username"]
    return HttpResponse("session deleted")