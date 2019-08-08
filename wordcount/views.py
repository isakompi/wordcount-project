from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    # for x in wordlist:
    #     x = x.upper()
    # print(x)
    upwod= [el.lower()for el in wordlist]
    wdic = {}
    for word in upwod:
        if word in wdic:
            #Increase
            wdic[word] +=1
        else:
            #add to dic
            wdic[word] =1
    swod = sorted(wdic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'swod':swod,'wordlist':wordlist})

def about(request):
    return render(request, 'about.html')