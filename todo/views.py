from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here
def say_hello(request):
    item = Item.objects.all()
    context = {
        'items' : item
    }
    return render(request, "todo/todo_list.html", context)


def add_item(request):  
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('say_hello')    
    form = ItemForm()
    context = {
        'form' : form
    }
    return render(request, "todo/add_item.html", context)



def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('say_hello') 
    form = ItemForm(instance=item)
    context = {
        'form' : form
    }
    return render(request, 'todo/edit_item.html', context)



def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('say_hello')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('say_hello')
