from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Advisor,Booking


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Advisor
        fields=['id','name','profile_pic']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'


