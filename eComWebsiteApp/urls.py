from django.urls import path
from .import views
urlpatterns  = [
    path('',views.homepageview,name="home"),
    path('about',views.aboutpageview,name="about"),
    path('contact',views.contactpageview,name="contact"),
    path('blogpost',views.blogpost,name="blogpost"),
    path('formdata',views.formdata,name="formdata"),
    path('getformdata/',views.getformdata,name="getformdata"),
    path('blog',views.blog,name='blog'),
    path('checkout',views.checkout,name='checkout'),
    path('productdetails',views.productdetails,name='productdetails'),
    path('products',views.products,name='products'),
    path('terms',views.terms,name='terms'),
    path('testimonials',views.testimonials,name='testimonials'),
]