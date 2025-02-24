from django.urls import path
from clothing import views  # Import views correctly

urlpatterns = [
    path('', views.clothing, name="clothing"),  # Clothing page
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),  # Edit product page
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),  # Delete product page (Fixed)
]
