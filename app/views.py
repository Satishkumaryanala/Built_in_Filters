from django.shortcuts import render
from datetime import datetime

# Create your views here.

def Built_in_filters(request):
    data = 'hAi HeLLo HOW aRe YOU'
    dt = datetime.now()
    cnt=5
    d={'data':data,'dt':dt,'cnt':cnt}
    return render(request,'Built_in_filters.html',d)