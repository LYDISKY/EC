from django.shortcuts import render
from django.views import View
#from django.templatetags.static import static
from app.models import Product
from app.forms import CustomerRegistrationForm
from django.contrib import messages


# Create your views here.
def base_view(request):
    return render(request,'app/base.html')
    
def home_view(request):
    return render(request,'app/home.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())


class ProductDetail(View):
    def get(self, request,pk):
        product=Product.objects.get(pk=pk)
        return render(request, 'app/product_detail.html', locals())

class CategoryTitle(View):
   def get(self, request, val):
    product = Product.objects.filter(title=val)
    #recuperer le title des produits de chaque valeur de category
    title = Product.objects.filter(category =product[0].category.values('title'))
    return render(request,"app/category.html",locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, 'app/registration.html', locals())


def post(self, request):
    form=CustomerRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Congratulations! User Registered Successfully")
    else:
        messages.warning(request, "Invalid Input Data")
    return render(request, 'app/registration.html', locals())

    

    