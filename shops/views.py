from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
from django.contrib import messages
from . models import Shopowner,Product
# Create your views here.
def product_viewer(request):
    return render(request,'products.html')

def shop_home(request):
    return render(request,'shops_homepage.html')

def signup_view(request):
    if request.method == 'POST':
        shopname = request.POST.get('shopname')
        ownername = request.POST.get('ownername')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        license_certificate = request.POST.get('license')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, "User already exists. Try another one")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email
                )
                shopowner = Shopowner.objects.create(
                    user=user,
                    shopname=shopname,
                    ownername=ownername,
                    phone=phone,
                    address=address,
                    license_certificate=license_certificate,
                    is_approved=False
                )
                messages.success(request, "Registration successful. Please wait for admin approval")
                return redirect('login')
        else:
            messages.error(request, "Passwords don't match")
    return render(request, 'shops_signup.html')

def add_products(request):
    if request.method == 'POST':
        product_company=request.POST.get('productcompany')
        product_name=request.POST.get('productname')
        product_type=request.POST.get('producttype')
        gear_transmission=request.POST.get('geartransmission')
        model_no=request.POST.get('modelno')
        quantity=request.POST.get('quantity')
        photo=request.FILES.get('photo')

        if product_type == 'EV' and gear_transmission == 'manual':
            messages.error(request,'EV cannot have manual transmission')
        elif Product.objects.filter(model_no=model_no).exists():
            messages.error(request,'A product with this model no exists.')
        else:
            new_product=Product(
                product_company=product_company,
                product_name=product_name,
                product_type=product_type,
                gear_transmission=gear_transmission,
                model_no=model_no,
                quantity=quantity,
                photo=photo,
                shop_owner=request.user
            )
            new_product.save()
            messages.success(request,'Product added successfully')
            return redirect('addproducts')
    return render(request,'shops_addproducts.html')

def view_products(request):
    products=Product.objects.filter(shop_owner=request.user)
    return render(request,'view_products.html',{'products':products})

def edit_products(request,id):
    product=Product.objects.get(id=id,shop_owner=request.user)
    if request.method == 'POST':
        quantity_to_add=int(request.POST.get('quantity'))
        photo=request.FILES.get('photo')
        if quantity_to_add:
            product.quantity=product.quantity+quantity_to_add
        if photo:
            product.photo=photo
        product.save()
        messages.success(request,'Updated successfully')
    return render(request,'edit_products.html',{'product':product})

def delete_product(request,id):
    product=Product.objects.get(id=id,shop_owner=request.user)
    quantity_to_delete=int(request.GET.get('quantity'))
    product.quantity=product.quantity-quantity_to_delete
    if product.quantity <=0:
        product.delete()
        messages.success(request,f'{product.product_name} has been deleted')
    else:
        product.save()
        messages.success(request,f'{quantity_to_delete} of {product.product_name} has been deleted')
    return redirect('viewproducts')