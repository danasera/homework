from django.urls import path

from product.views import ProductsListView, ProductDetailView, CreateProductView, UpdateProductView, DeleteProductView, \
    ProductViewSet, product_details, create_product, delete_product, update_product, patch_product, \
    first_product

urlpatterns = [
    path('prod/', first_product),
    path('prod/<int:pk>/', product_details),
    path('prod/create/', create_product),
    path('prod/delete/<int:pk>/', delete_product),
    path('prod/update/<int:pk>/', update_product),
    path('prod/update1/<int:pk>/', patch_product),

    path('products/', ProductsListView.as_view()),
    path('products/detail/<int:pk>/', ProductDetailView.as_view()),
    path('products/create/', CreateProductView.as_view()),
    path('products/update/', UpdateProductView.as_view()),
    path('products/delete/', DeleteProductView.as_view()),

    path('products/', ProductViewSet.as_view({'get': 'list',
                                          'post': 'create'})),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'})),



    ]