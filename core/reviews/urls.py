from django.urls import path
from .views import (
    ProductListCreateView,
    ProductDetailView,
    ReviewCreateView,
    ProductReviewsListView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:product_id>/reviews/', ProductReviewsListView.as_view(), name='product-reviews'),
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
]