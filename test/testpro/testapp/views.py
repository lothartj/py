from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Items
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
# Create your views here.
def itemview(request, ):
    items =  Items.objects.all()
    return render(request, 'testapp/itemview.html', {'items':items})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('main')


    return render(request, 'testapp/login.html')

def main(request):
    if request.method == 'POST':
        itemno = request.POST.get('itemno')
        itemdescription = request.POST.get('itemdescription')
        itembarcode = request.POST.get('itembarcode')
        itemuom = request.POST.get('itemuom')

        if not itemno or not itemdescription or not itembarcode or not itemuom:
            messages.error(request, 'Please fill in all the fields')
        else:
            item = Items(itemno=itemno,itemdescription=itemdescription,itembarcode=itembarcode,itemuom=itemuom)
            item.save()
            messages.success(request, 'item Save')

    return render(request, 'testapp/main.html')

def itemitself(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    return render(request, 'testapp/itemitself.html', {'item':item})


def itemdelete(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Items, id=item_id)
        item.delete()
    return redirect('itemview')
