from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'listings', views.ListingViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'bookings', views.BookingViewSet)
# The API URLs are now determined automatically by the router.
urlpatterns = router.urls   
