from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

from .models import Item    

# Create your views here.

class Display(View):
    def homeDisplay(request):
        context= {
            'page_name': "Home page",
            "items": Item.objects.all()[:5]
        }
        return render(request, 'owner/index.html', context)