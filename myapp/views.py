from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from payment.models import Payment
from  django.conf import settings

# Create your views here.


def products(request):
    page_obj=products = Product.objects.all()
    product_name =request.GET.get('product_name')
    if product_name!='' and product_name is not None:
        page_obj= products.filter(name__icontains =product_name)
    paginator= Paginator(page_obj, 3)
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context ={
      'page_obj':page_obj  
    }
    return render(request, 'myapp/index.html', context)




def product_detail(request, id):
  if request.method == 'POST':
      product_id = request.POST.get('product_id')
      user_id = request.POST.get('user_id')
      price = request.POST.get('price')
      email = request.POST.get('email')
      order = Payment(product_id= product_id, user_id = user_id, amount=price, email=email, )
      order.save()
      context={
       'order':order,
       'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
      }   
      return render(request, 'payment/makepayment.html', context, )
  product= Product.objects.get(id=id)
  context={
       'product':product
   }        
  return render(request, 'myapp/detail.html', context)
    

@login_required

def add_product(request):

  if request.method == 'POST':
      name = request.POST.get('name')
      price = request.POST.get('price')
      desc = request.POST.get('desc')
      image = request.FILES['uploads']
      seller_name=request.user
      product = Product(name=name, price=price, desc=desc,image=image, seller_name= seller_name)
      product.save()

     
  return render(request, 'myapp/addproduct.html')



def update_product(request, id):
  product= Product.objects.get(id=id)
  if request.method == 'POST':
    product.name =request.POST.get('name') 
    product.price =request.POST.get('price') 
    product.desc =request.POST.get('desc') 
    product.image =request.FILES['uploads'] 
    product.save() 
    return redirect('/myapp/products')
  context ={

    'product':product
  }
  return render(request, 'myapp/updateproduct.html', context)


def delete_product(request,id):
      product = Product.objects.get(id=id)
      context={
        'product':product,
      }
      if request.method == 'POST':
        product.delete()
        return redirect('/myapp/products')
      return render(request, 'myapp/delete.html', context)

def my_listings(request):
    product =Product.objects.filter(seller_name=request.user)
    context ={
      'products': product,
    }
    return render(request, 'myapp/mylistings.html', context )