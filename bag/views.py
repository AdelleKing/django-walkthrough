from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url') 
    #redirect_url uses the hidden url in the bag.html page which stores where 
    #the user selected an item and returns them to that page.
    bag = request.session.get('bag', {}) 
    #this variable will look to see if there is a session in progress. 
    #Session stores the information until the client and server are finished communicating/ the user closes their browser.
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:       
        bag[item_id]=quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)