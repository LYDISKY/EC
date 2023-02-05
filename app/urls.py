from . import views
from django.conf import settings 
from django.templatetags.static import static
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('base/',views.base_view, name='base'),
    path('home/',views.home_view, name ='home'),
    path('category/', views.CategoryView.as_view(),name='category'),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path('proddetail/<int:pk>', views.ProductDetail.as_view(), name='proddetail'),
    path('category-title/<val>', views.CategoryTitle.as_view(), name='category-title'),
    path('registration/', views.CustomerRegistrationView.as_view(), name="costomerRegistration")
]#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#importer settings et static 



