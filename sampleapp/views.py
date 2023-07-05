from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 
from .models import Category,Product,Relatedimage,Contact,Cart
from django.contrib import messages
import decimal
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,SigninForm
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.core.mail import send_mail 



# Create your views here.
def home(request):
    return render(request,'index.html')


def contact_page(request):
    if request.method=='POST':
        email=request.POST['email']
        mssg=request.POST['msg']
        Contact(email=email,message=mssg).save()
        send_mail(subject='thankyou',message='thankyou for contacting us',from_email=settings.EMAIL_HOST_USER,recipient_list=[email,],fail_silently=False)
        messages.info(request,'email already exsist')

    return render(request,'contact.html')

def about(request):
    return render(request,"about.html")
def blog (request):
    return render(request,"blog.html")

def regpage(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            messages.info(request,'user saved succesfully')
        else:
            messages.info(request,'invalid')
    else:
        form=SignupForm()
    context={
        'form':form
    }
    
    return render(request,'registration.html',context)

def loginpage(request):
    if request.method=='POST':
        form=SigninForm(request.POST)
        username=form['username'].value()
        password=form['password'].value()
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,'login sucess')
            return redirect('cart')
        else:
            messages.info(request,'invalid')  
    else:
        form=SigninForm()
    context={
        'form':form

    }
        
    return render(request,'login.html',context)

def contact (request):
    return render(request,"contact.html")



def category(request):
    categories=Category.objects.filter(is_active=True)
    return render(request,"category.html",{'categories':categories})


def category_products(request,slug):
    category=get_object_or_404(Category, slug=slug)
    products=Product.objects.filter(is_active=True, category=category)
    categories=Category.objects.filter(is_active=True)
    context={
        'category':category,
        'products':products,
        'categories':categories,
    }
    return render(request,'category_products.html',context)

def detail_page(request,slug):
      product=get_object_or_404(Product,slug=slug,)
      relatedimages=Relatedimage.objects.filter(products=product.id)

      context={
         'product': product,
         'relatedimages':relatedimages,
    }
      return render(request, 'related.html', context)

@login_required
def cart(request):
    user=request.user
    cart_products=Cart.objects.filter(user=user)
    amount=decimal.Decimal(0)
    shipping_amount=decimal.Decimal(10)
    cp=[p for p in Cart.objects.all() if p.user==user]
    if cp:
         for p in cp:
             temp_amount=(p.quantity * p.product.price)
             amount+=temp_amount
    context = {
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount,

    }
    return render(request,'cart.html',context)

@login_required
def add_to_cart(request):
    user=request.user
    print(request.user)
    product_id=request.GET.get('prod_id')
    product=get_object_or_404(Product, id=product_id)
    item_already_in_cart=Cart.objects.filter(product=product_id, user=user)
    if item_already_in_cart:
        cp=get_object_or_404(Cart, product=product_id, user=user)
        cp.quantity += 1
        cp.save()
        
    else:
        Cart(user=user,product=product).save()
        return  redirect('cart')
    return  redirect('cart')







@login_required
def pluscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.quantity += 1
        if cp.quantity>=cp.product.productStock:
            cp.quantity -= 1
        cp.save()

    return redirect('cart')
@login_required
def minuscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        if cp.quantity==1:
            cp.delete()
        else:
            cp.quantity-=1
            cp.save()
    return redirect('cart')


def deletecart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.delete()
    return redirect('cart')

def search(request):
    q = request.GET.get('q','')
    data = Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request, 'search.html', {'data': data})