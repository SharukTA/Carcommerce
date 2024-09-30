from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from shops.models import Shopowner,Product
from . models import Customer,Wishlist

# Create your views here.
def index(request):
    return render(request,'index.html')

def services(request):
    return render(request,'services.html')

def shopview(request):
    shops=Shopowner.objects.all()
    return render(request,'shops_view.html',{'shops':shops})

def register_view(request):  
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')
        if password == confirm_password:
            try:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=email
                )
                customers=Customer.objects.create(
                    user=user,
                    phone=phone,
                    address=address
                ) 
                messages.success(request,"Registration successfull. Please login")
                return redirect('login')
            except Exception as e:
                messages.error(request,"Invalid inputs or user already exists")
        else:
            messages.error(request,"Passwords does not match")
    return render(request,'customer_signup.html')

def edit_profile(request):
    user=request.user
    if request.method == 'POST':
        if hasattr(user,'shopowner_profile'):
            shopname=request.POST.get('shopname')
            ownername=request.POST.get('ownername')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            password=request.POST.get('password')
            conpass=request.POST.get('confirmpassword')
            licence=request.FILES.get('license')
            if password == conpass:
                try:
                    user.shopowner_profile.shopname=shopname
                    user.shopowner_profile.ownername=ownername
                    user.shopowner_profile.phone=phone
                    user.shopowner_profile.address=address
                    if password:
                        user.set_password(password)
                    if licence:
                        user.shopowner_profile.license_certificate=licence
                    user.shopowner_profile.save()
                    user.save()
                    messages.success(request,'Profile updated successfully')
                except Exception as e:
                    messages.error(request,'User already exists')
            else:
                messages.error(request,'Passwords does not match')
        
        elif hasattr(user,'customer_profile'):
            username=request.POST.get('username')
            email=request.POST.get('email')
            phone_no=request.POST.get('phone')
            adress=request.POST.get('address')
            passwords=request.POST.get('password')
            confirmpass=request.POST.get('confirmpassword')
            if passwords == confirmpass:
                try:
                    user.username=username
                    user.email=email
                    user.customer_profile.phone=phone_no
                    user.customer_profile.address=adress
                    if passwords:
                        user.set_password(passwords)
                    user.customer_profile.save()
                    user.save()
                    messages.success(request,'Profile updated successfully')
                except Exception as e:
                    messages.error(request,'User already exists')
            else:
                messages.error(request,'Passwords does not match')
    return render(request,'edit_profile.html')

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            try:

                if hasattr(user,'shopowner_profile'):
                    shopowner=user.shopowner_profile
                    if not shopowner.is_approved:
                        messages.error(request,"Please wait for admin approval")
                        return render(request,'login.html')
                                            
                    login(request,user)
                    return redirect('shopshome')
                    
                elif hasattr(user,'customer_profile'):
                    login(request,user)
                    return redirect('products') 
                    
            except Shopowner.DoesNotExist:
                messages.error(request,"No associated shopowners")
                return redirect('login')
            except Customer.DoesNotExist:
                messages.error(request,"No associated customers")
                return redirect('login')

        else:
            messages.error(request,"Invalid username or password")
    return render(request,'login.html')

def customerproduct_view(request):
    products=Product.objects.all()
    return render(request,'customer_productview.html',{'products':products})

def add_to_wishlist(request,id):
    product=Product.objects.get(id=id)
    Wishlist.objects.create(user=request.user,product=product)
    messages.success(request,f'{product.product_name} added to the wishlist')
    return redirect('customerproductview')

def wishlist(request):
    wishlist_items=Wishlist.objects.filter(user=request.user)
    context={
        'wishlist_items':wishlist_items
    }
    return render(request,'customer_cart.html',context)

def remove_from_wishlist(request,id):
    product=Wishlist.objects.get(id=id)
    product.delete()
    messages.success(request,f'{product.product_name} has been removed from wishlist')
    return redirect('wishlist')

def sign_out(request):
    logout(request)
    return redirect('home')