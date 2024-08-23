from django.contrib import admin
from .models import Appointment

#sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.
class AppointmentClass(admin.ModelAdmin):
    list_display = ["patient_first_name", "doctor_first_name", "appointment_status", "appointment_type", "symptom", "time"]

    def patient_first_name(self, obj):
        return obj.patient.user.first_name
    
    def doctor_first_name(self, obj):
        return obj.doctor.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        
        if obj.appointment_status == "Running" and obj.appointment_type == "Online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin.html', {'user': obj.patient.user, 'doctor': obj.doctor})

            email = EmailMultiAlternatives(email_subject, '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()


admin.site.register(Appointment, AppointmentClass)