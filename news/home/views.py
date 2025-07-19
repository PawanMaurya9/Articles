from django.shortcuts import render

# Create your views here.
from .data import articles_data

from django.http import HttpResponse

from gtts import gTTS

import os

from news.settings import BASE_DIR

def num(r): 
    return render(r, 'home.html', {'a': articles_data, "c":1})

def next(r,id):

    for i in articles_data:

        if i['id']==id:
            print(id) 
            k=i["content"] 
            l=i["title"] 
            n=i['id'] 
            #red-gTTS(k, 'en') 
            # #ed.save("id.mp3") 
            # #os.system("start id.mp3")

        break 
    return render(r, 'nextpage.html',{'a':i["content"], 'b':i["title"], 'e':i["id"]})


def recorder(r,id):
    for i in articles_data:
        if i['id'] == id:
            a = gTTS(i['content'],lang='en')
            pth = os.path.join("audiofile",f"audio_{i["id"]}.mp3")
            a.save(pth)
            with open(pth,'rb') as f:
                audio_data = f.read()
                return HttpResponse(audio_data,content_type='audio/mp3')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def solution(request):
    return render(request,'help.html')

