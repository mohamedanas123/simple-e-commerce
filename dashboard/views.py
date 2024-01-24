from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from items.models import Item
from .forms import EditItemForm

@login_required(login_url='login')

def dashboard(request):
    item=Item.objects.filter(created_by=request.user)
    return render(request,'dashboard/dash.html',context={
        'item':item
    })

@login_required(login_url='login')
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard')

@login_required(login_url='login')
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method=='POST':
        
        form=EditItemForm(request.POST,request.FILES,instance=item)# request.files for render a image and instance is for updating the form

        if form.is_valid():
            item.save()

            return redirect('detail',pk=item.id)
    form=EditItemForm(instance=item)
    return render(request,'dashboard/edit.html',context={
        'form':form
    })




