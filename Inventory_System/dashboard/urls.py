from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('customer/', views.CustomerView.as_view(),
         name='dashboard-customer'),
    path('product/', views.ProductView.as_view(),
         name='dashboard-product'),
    path('customer/registration', views.CustomerRegistrationView.as_view(),
         name='dashboard-register-customer'),
    path('product/registration', views.ProductRegistrationView.as_view(),
         name='dashboard-register_prod'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(),
         name='dashboard-update-prod'),
    path('customer/update/<int:pk>/', views.CustomerUpdateView.as_view(),
         name='dashboard-update-customer'),
    path('orders/', views.OrderView.as_view(),
         name='dashboard-order'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
