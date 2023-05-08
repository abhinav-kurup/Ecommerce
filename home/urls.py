from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('add_cart', views.add_cart, name="add_cart"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('http/', views.http, name='http'),
    path('checkout/',views.checkout,name='checkout'),
    path('checkout/shipping/',views.shipping,name='shipping'),
    path('logout/',views.logout_view,name='logout')
]