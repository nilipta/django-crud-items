from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views import View
from django.db import models
from django.forms import ModelForm
from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.contrib.auth.decorators import login_required, permission_required
# from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView

from .models import Item

# Create your views here.

class Display(View):
    def homeDisplay(request):
        context= {
            'page_name': "Home page",
            "items": Item.objects.all(),
            "logged_in_username": request.user.username 
        }
        print(request.user.has_perm)
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

class DeleteItemClass:
    def deleteHandler(request, pk): # this pk is the argument from index.htm & urls.py
        toBeDeletedItem = Item.objects.get(pk=pk)
        toBeDeletedItem.delete()
        return HttpResponseRedirect(reverse('owner:owner-home'))

# automatically loads item_confirm_delete.html as it is a edfault template style
# @permission_required('owner.can_delete_item')
# @method_decorator(permission_required, name='owner.can_delete_item')
class DeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Item
    permission_required = 'owner.can_delete_item'
    context_object_name = 'item'
    success_url = reverse_lazy('owner:owner-home')


class EditFormClass:
    def editHandler(request, item_id):
        toBeEditedItem = Item.objects.get(pk=item_id)
        itemImagePath = toBeEditedItem.item_image   #only added to show image in UI

        if request.method == 'POST':
            form = ItemForm(request.POST, request.FILES, instance=toBeEditedItem)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/owner')
        else:
            form = ItemForm(instance=toBeEditedItem)

        return render(request, 'owner/editItem.html', {'form': form, 'itemImagePath':itemImagePath})