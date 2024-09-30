
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('services',views.services,name='services'),
    path('shopview',views.shopview,name='shopview'),
    path('customersignup',views.register_view,name='customersignup'),
    path('editprofile',views.edit_profile,name='editprofile'),
    path('login',views.login_view,name='login'),
    path('customerproductview',views.customerproduct_view,name='customerproductview'),
    path('addtowishlist/<int:id>',views.add_to_wishlist,name='addtowishlist'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('removefromwishlist/<int:id>',views.remove_from_wishlist,name='removefromwishlist'),
    path('logout',views.sign_out,name='logout')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
