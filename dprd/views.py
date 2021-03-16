from django.shortcuts import render


def index(request):
    context = {
        'title':'DPRD|DELI SERDANG',
        'subtitle':'DPRD',
    }
    return render(request,'index.html',context)