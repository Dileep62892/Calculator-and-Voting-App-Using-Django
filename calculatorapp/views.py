from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def calculator(request):
    return render(request, 'views/calculator.html')


def submitquery(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        mydict = {
            "q" : q,
            "ans" : ans,
            "error" : False,
            "result" : True,
        }
        return render(request,'views/calculator.html',context=mydict)
    except:
        mydict = {
            "error" : True,
            "result" : False,
        }
        return render(request,'views/calculator.html',context=mydict)


