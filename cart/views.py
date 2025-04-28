from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def cart_detail(request):
    # Логика отображения корзины
    return render(request, 'cart/detail.html')

def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Логика добавления в корзину
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Логика удаления из корзины
    return redirect('cart:cart_detail')