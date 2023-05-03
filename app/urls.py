from django.urls import path
from app import views
urlpatterns = [
    path('about',views.Abouts,name='about'),
    path('',views.Home,name="home"),
    path('usecase/<str:pk>',views.Usecase,name="usecase"),
    path('products/<str:pk>',views.Products,name="products"),
    path('productdetails/<int:pk>',views.Productdetails,name="productdetails"),
    path('contact',views.Contact,name='contact'),
    path('companys/', views.Companys, name='companys'),

    

]
