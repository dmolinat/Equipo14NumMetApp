from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import CookieCountMethodUse, UserCookie
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

@csrf_exempt 
def create_cookie_method(request):
    if request.method == "POST":
        try:
            method_name=json.loads(request.body)
            
            coockie_count_obj=CookieCountMethodUse(
                method=method_name["method"]
            )
            coockie_count_obj.save()
            
            return JsonResponse(
                {"message": "Contador usos de metodo por cookie creado"}, status=201
                )
        except:
            return JsonResponse(
                {"message": "ERROR: En creacion de contador por metodo"}, status=401
                )

def confirm_cookie(request):
    if request.method == "POST":
        try:
            buttom_value=request.POST.get('confirm', None)
            if(buttom_value=="Yes"):
                cookie_act=True
            else:
                cookie_act=False
                
            user_cookie_obj=UserCookie(
                    user=request.user,
                    cookie_active=cookie_act,
                    date_use=datetime.datetime.today()
                )
            user_cookie_obj.save()            
            return redirect('home')
        except:
            return redirect('logout')
    else:
        return render(request, 'cookie/cookie_confirm.html')
    
            
