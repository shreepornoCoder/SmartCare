from django.shortcuts import render
from doctor import models, serializers
from rest_framework import viewsets, pagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import BaseFilterBackend


# Create your views here.
class DoctorPaginition(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_params = page_size
    max_page_size = 100

class AvailableTimeForDoctor(filter.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specializations.objects.all()
    serializer_class = serializers.SpecializationsSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForDoctor]

class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Doctor.objects.all()
    pagination_class = DoctorPaginition
    serializer_class = serializers.DoctorSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer