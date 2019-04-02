from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def count(request):
    ft=request.GET['fulltext']
    wc=ft.split()
    worddictionary={}

    for word in wc:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word]=1



    return render(request,'count.html',{'fulltext':ft,'count':len(wc),'worddictionary':worddictionary.items()})