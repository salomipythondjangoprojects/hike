from django.urls import path
from . import views



urlpatterns=[
    path('',views.home,name='home'),
    

    path('shoping-cart',views.cart,name='cart'),
    path('about',views.about,name="about"),
    path('blog',views.blog,name='blog'),
    
    path('registration',views.regpage,name='regpage'),
    path('login',views.loginpage,name='login'),

    
    
    path('contact',views.contact_page,name='contact_page'),
    
    
    
    
    path('pluscart/<int:cart_id>/',views.pluscart,name='pluscart'),
    path('minuscart/<int:cart_id>/',views.minuscart,name='minuscart'),
    path('deletecart/<int:cart_id>/',views.deletecart,name='deletecart'),

    path('category',views.category,name="category"),
    path('<slug:slug>',views.category_products,name='category_products'),
    path('product/<slug:slug>/',views.detail_page,name='detail_page'),

    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('search/',views.search,name='search'),


  
]