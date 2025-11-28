
      
      
      
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('about/', views.about, name="about"),
    path('about/product1/', views.product1, name="about_product1"), 
    path('about/product2/', views.product2, name="about_product2"), 
    path('about/product3/', views.product3, name="about_product3"), 
    path('about/product4/', views.product4, name="about_product4"), 
    path('about/product5/', views.product5, name="about_product5"), 
    path('about/product6/', views.product6, name="about_product6"), 
    path('about/product7/', views.product7, name="about_product7"), 
    path('about/product8/', views.product8, name="about_product8"), 
    path('about/product9/', views.product9, name="about_product9"), 
  
    path('contact/', views.contact, name="contact"),
    path('cart/', views.cart, name="cart"),
    path('tv/', views.tv, name="tv"),
    path('Iphone/', views.iphone_list, name="iphone_list"),
    path('navbar/', views.navbar, name='navbar'),
    path('signup/', views.SignupPage, name="signup"),
    path('login/', views.LoginPage, name="login"), 
    path('homeimg1/', views.homeimg1, name="homeimg1"), 
    path('homeimg2/', views.homeimg2, name="homeimg2"), 
    path('homeimg3/', views.homeimg3, name="homeimg3"),
    path('home2/', views.home2, name="home2"), 
    path('ToolsThree/', views.ToolsThree, name="ToolsThree"), 
    path('ToolsTwo/', views.ToolsTwo, name="ToolsTwo"), 
    path('Tools/', views.Tools, name="Tools"), 
    path('footer/', views.footer, name="footer"), 
    path('product1/', views.product1, name="product1"), 
    path('product2/', views.product2, name="product2"), 
    path('product3/', views.product3, name="product3"), 
    path('product4/', views.product4, name="product4"), 
    path('product5/', views.product5, name="product5"), 
    path('product6/', views.product6, name="product6"), 
    path('product7/', views.product7, name="product7"), 
    path('product8/', views.product8, name="product8"), 
    path('product9/', views.product9, name="product9"), 
    path('product10/', views.product10, name="product10"), 
    path('product11/', views.product11, name="product11"), 
    path('logout/', views.LogoutPage, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
