from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

urlpatterns = router.urls

# if you want add some more path to your urlpatterns, code like below
# urlpatterns = [
#     path('', include(router.urls)),
#     path()
# ]
