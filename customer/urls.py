from rest_framework.routers import DefaultRouter

from customer.views import CustomerViewSet

router = DefaultRouter()

router.register(r'customer', CustomerViewSet)