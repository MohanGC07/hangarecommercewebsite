from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json

def index(request):
   allProds=[]
   catprods=Product.objects.values('category','id')
   cats={item ['category']for item in catprods}
   for cat in cats:
      prod=Product.objects.filter(category=cat)
      n=len(prod)
      nSlides=n//4+ceil((n/4)-(n//4))
      allProds.append([prod,range(1,nSlides),nSlides])
   params={'allProds':allProds}

   return render(request,'shop/index.html',params)

def about(request):
   
   return render(request,'shop/about.html')

def all(request):
   return render(request,'shop/all.html')

def contact(request):
   if request.method=="POST":
      name=request.POST.get('name','')
      email=request.POST.get('email', '')
      phone=request.POST.get('phone', '')
      desc=request.POST.get('desc', '')
      print(name,email,phone, desc )
      contact=Contact(name=name,email=email,phone=phone,desc=desc)
      contact.save()
      
   return render(request,'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')

        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse(f'exception{e}')

    return render(request, 'shop/tracker.html')

def searchMatch(query, item):
    if not item:
        return False
    searchable_fields = (item.product_name, item.category, item.description)
    return any(query in (field or "").lower() for field in searchable_fields)


def search(request):
    query = request.GET.get('search', '').strip().lower()

    if not query or len(query) < 4:
        return render(request, 'shop/index.html',
                      {'msg': "Please make sure to enter relevant search query"})

    allProds = []
    categories = Product.objects.values_list('category', flat=True).distinct()
    for cat in categories:
        products = Product.objects.filter(category=cat)
        matched = [item for item in products if searchMatch(query, item)]
        if matched:
            n = len(matched)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([matched, range(1, nSlides), nSlides])

    params = {'allProds': allProds, 'msg': ""} if allProds \
        else {'msg': "No products found matching your search."}
    return render(request, 'shop/index.html', params)

def productview(request,myid):
   # fetch the products using id
   product=Product.objects.filter(id=myid)
   print(product)
   return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')
