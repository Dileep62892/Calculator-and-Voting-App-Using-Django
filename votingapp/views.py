from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

arr = ['C','C++','C#','Python','Java','JavaScript','Ruby','PHP','Perl','Objective-C','Swift','TypeScript']
globalcnt = dict()

def index(request):
    mydict1 = {
        "arr" : arr,
    }
    return render(request,'views/index.html',context=mydict1)

def getquery(request):
    q = request.GET['languages']
    if q in globalcnt:
        globalcnt[q]+=1
    else:
        globalcnt[q]=1
    
    mydict1={
        "arr" : arr,
        "globalcnt" : globalcnt,
    }
    return render(request,'views/index.html',context=mydict1)


def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(), key=lambda x:x[1], reverse=True))
    mydict1 = {
        "arr" : arr,
        "globalcnt" : globalcnt,
    }
    return render(request,'views/index.html',context=mydict1)



