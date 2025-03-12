from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path(
        "products/",
        views.ProductListCreateAPIView.as_view(),
        name="product-list-create"
    ),    
    path(
        "product-info/",
        views.ProductInfoAPIView.as_view(),
        name="product-info"
    ),   
    path(
        "products/<int:product_id>/",
        views.ProductDetailAPIView.as_view(),
        name="product-detail"
    ),
    path(
        "users/",
        views.UserListView.as_view(),
        name="users"
    )
    
    
]

router = DefaultRouter()
router.register('orders', views.OrderViewSets)
urlpatterns += router.urls
