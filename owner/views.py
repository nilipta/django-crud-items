from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views import View
from django.db import models
from django.forms import ModelForm

from .models import Item

# Create your views here.

class Display(View):
    def homeDisplay(request):
        context= {
            'page_name': "Home page",
            "items": Item.objects.all()
        }
        return render(request, 'owner/index.html', context)


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'visibleToCostumer', 'profitPercentage', 'timeStamp', 'item_image']

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['item_image'].required = False


class AddFormClass:
    def get_name(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ItemForm(request.POST, request.FILES)    #request.FILES is needed to store the file in static folder and in database also
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                print("Item details = ", form.cleaned_data)
                form.save()
                # redirect to a new URL:
                # return HttpResponse('/thanks/')   $todo: add latter a success message on screen
                return HttpResponseRedirect('/owner')


        # if a GET (or any other method) we'll create a blank form
        else:
            form = ItemForm()

        return render(request, 'owner/addItem.html', {'form': form})