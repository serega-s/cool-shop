from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('become-vendor/', views.become_vender, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-vendor/', views.edit_vendor, name="edit_vendor"),
    path('edit-product/<int:pk>/', views.edit_product, name="edit_product"),
    path('<int:vendor_id>/', views.vendor, name='vendor'),
    path('', views.vendors, name="vendors"),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login')

]
