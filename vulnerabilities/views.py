from django.shortcuts import render
from django.http import HttpResponse

from .models import Admin

# Create your views here.


def sql_injection(request):
    if "password" in request.GET:
        p = " ".join(request.GET["password"].split("&"))
        print(p)
        admin = Admin.objects.raw(f"SELECT * FROM vulnerabilities_admin WHERE password='{ p }'")[0]

        if admin:
            return HttpResponse(f"Autenticato! \n{ admin }")
    else:
        return HttpResponse("Devi autenticarti")


def xss(request):
    if "data" in request.GET:
        return HttpResponse(f"Ciao! { request.GET['data'] }")
    else:
        return HttpResponse("Inserisci dei dati")
