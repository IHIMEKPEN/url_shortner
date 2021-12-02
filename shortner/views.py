from django.shortcuts import render
import pyshorteners 

# Create your views here.
def index(request):
    return render(request, 'shortner/index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        s = pyshorteners.Shortener()
        shorten_url=s.tinyurl.short(link)
        print(shorten_url)
        context={
            "url":shorten_url
        }       
        return render(request,'shortner/index.html',context)

