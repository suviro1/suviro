from django.shortcuts import redirect, render
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.
from .form import ContactForm
from django.contrib import messages

def Home(request):
    return render(request, 'home.html')


def Usecase(request, pk):
    usecase_list = Usecases.objects.filter(category=pk)
    paginator = Paginator(usecase_list, 10)  # Show 10 usecases per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'usecase.html', {'page_obj': page_obj})

def Products(request,pk):
    products  = Product.objects.filter(category=pk)
    nav = ProductCategory.objects.filter(company__in=[p.category.company for p in products])
    



    items_per_page = 10
    paginator = Paginator(products, items_per_page)

    # Get the current page number from the query string
    page_number = request.GET.get('page')

    # Get the current page object from the Paginator
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'nav':nav
    }
    return render(request, 'products.html', context)



def productscategory(request,pk):
    pc = ProductCategory.objects.filter(company=pk)
    return render(request,'productscategory.html',{'pc':pc})



def Companys(request):
    comp = Company.objects.all().values('id','name')
    return JsonResponse({'comp': list(comp)})

def About(request):
    return render(request , 'about.html')

def Productdetails(request,pk):

    product = Product.objects.get(pk=pk)

    return render(request , 'productdetails.html', {'product': product})






def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the Contact object and redirect to a success page
            contact = form.save()
            messages.success(request, 'Your message was sent successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
