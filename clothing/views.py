from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# Define the missing clothing view
def clothing(request):
    pro_img = Product.objects.all()
    return render(request, "clothing/fashion.html", {"pro_img": pro_img})

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('clothing')  
    else:
        form = ProductForm(instance=product)

    return render(request, "clothing/edit_product.html", {"form": form, "product": product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('clothing')

    return render(request, "clothing/confirm_delete.html", {"product": product})
