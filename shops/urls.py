
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('products/',views.product_viewer,name='products'),
    path('shopsignup/',views.signup_view,name='shopsignup'),
    path('shopshome/', views.shop_home, name='shopshome'),
    path('addproducts/', views.add_products, name='addproducts'),
    path('viewproducts/', views.view_products, name='viewproducts'),
    path('editproducts/edit/<int:id>/', views.edit_products, name='editproducts'),
    path('deleteproducts/<int:id>/', views.delete_product, name='deleteproducts')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
