from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')
product_router.register(
    'images', views.ProductImageViewSet, basename='product-images')

cart_item_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_item_router.register(
    'items', views.CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + product_router.urls + cart_item_router.urls

# if you want add some more path to your urlpatterns, code like below
# urlpatterns = [
#     path('', include(router.urls)),
#     path()
# ]
