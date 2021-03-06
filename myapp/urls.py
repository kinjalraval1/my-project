from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('new_password/',views.new_password,name='new_password'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('seller_change_password/',views.seller_change_password,name='seller_change_password'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
    path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
    path('seller_delete_product/<int:pk>/',views.seller_delete_product,name='seller_delete_product'),
    path('product_filter/<str:pc>/',views.product_filter,name='product_filter'),
    path('user_product_detail/<int:pk>/',views.user_product_detail,name='user_product_detail'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('pay/',views.initiate_payment,name='pay'),
    path('callback/', views.callback, name='callback'),
    path('ajax/validate_email/',views.validate_email,name='validate_email'),
    path('search/',views.search,name='search'),
    path('order/',views.order,name='order'),

]
 