from django.urls import path
from .views import ProdutoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = router.urls