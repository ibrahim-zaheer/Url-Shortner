from django.shortcuts import render
from django.http import HttpResponse
from .forms import URLForm
from datetime import datetime
import random, string
from .models import ShortURL
# Create your views here.
def hello(request):
    return render(request,"home.html")

def creatingUrl(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars=''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortURL.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            d = datetime.now()
            s = ShortURL(original_url=original_website, short_url=random_chars, time_date_created=d)
            s.save()
            return render(request,'UrlCreated.html',{'short_url':random_chars,'original_url':original_website})
    else:
        form = URLForm()
        return render(request,"create.html",{"form":form})    

def redirect(request, url):
    current_obj = ShortURL.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj':current_obj[0]}
    return render(request, 'redirect.html', context)

def showAll(request):
    current_obj = ShortURL.objects.all()
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'objs':current_obj}
    return render(request, 'showAll.html', context)