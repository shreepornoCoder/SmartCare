from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('doctor', views.DoctorViewSet)
router.register('specialization', views.SpecializationViewSet)
router.register('designation', views.DesignationViewSet)
router.register('avaible_time', views.AvailableTimeViewSet)
router.register('review', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]
