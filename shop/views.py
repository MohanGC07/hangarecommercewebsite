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
    if item:
        if query in item.description.lower() or query in item.product_name.lower() or query in item.category.lower():
            return True
    return False


def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if query in searchMatch(query,item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg":""}
    if len(allProds)==0 or len(query)<4:
        params={'msg':"Please make sure to enter relevant search query"}
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

def verify_payment(request)

url = "https://khalti.com/api/v2/payment/verify/"

payload = {
  'token': 'QUao9cqFzxPgvWJNi9aKac',
  'amount': 1000
}

headers = {
  'Authorization': 'Key test_secret_key_f59e8b7d18b4499ca40f68195a846e9b'
}

response = requests.request("POST", url, headers=headers, data=payload)