from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,Category
from django.db.models import Q 
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm
import json


class items(ListView):
    model=Item
    template_name='item/browse.html'
    context_object_name='items'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['qs_json']=json.dumps(list(Item.objects.values('id','category','name','description','price','image')))
        return context
    
'''def itemss(request):
    category_id=request.GET.get('category',0)
    category=Category.objects.all()
    if cca'''

def detail(request,pk):
    items=get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(category=items.category,is_sold=False).exclude(pk=pk)[0:7]
    return render(request,'item/detail.html',context={
        'item':items,
        'r_items':related_items
    })


@login_required(login_url='login')
def new(request):
    if request.method=='POST':
        form=NewItemForm(request.POST,request.FILES)# request.files for render a image
        if form.is_valid():
            item=form.save(commit=False)# it for save the form and we can define extra information before adding to the databases
            item.created_by=request.user
            item.save()

            return redirect('detail',pk=item.id)
    form=NewItemForm()
    return render(request,'item/newitem.html',context={
        'form':form
    })

