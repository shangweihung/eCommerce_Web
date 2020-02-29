from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product 
from cart.forms import CartAddProductForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def product_list(request, category_slug = None ): 
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {    # containing the data to insert into the placeholders. 
        'category': category,
        'categories': categories,
        'products': products
    }
    

    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, available=True)
    cart_product_form = CartAddProductForm()

    categories = Category.objects.all()
    
    context = {  # containing the data to insert into the placeholders. 
        'product': product,
        'cart_product_form': cart_product_form,
        'categories': categories
    }

    return render(request, 'shop/product/detail.html', context)
    

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})



def register(request):
    if request.method == 'POST':

    	# Assigning the User Creation form with the Post request object to form variable
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user
            form.save()
            # Getting the values from the form
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authenticate user using the authenticate method
            user = authenticate(username=username, password=raw_password)

            # After Successfully Authenticated then use login function to login the user

            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def story(request):
    return render(request, 'shop/story.html', {})
