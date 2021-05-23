from django import http
from django.shortcuts import render
from .models import Advisor,Booking
from .serializers import AdvisorSerializer,BookingSerializer
from rest_framework.views import APIView
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import datetime

class advisorView(viewsets.ModelViewSet):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer

class bookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class AdvisorView(APIView):
    def post(self,request):
        data=request.data
        serializer=AdvisorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

from rest_framework_simplejwt.tokens import RefreshToken


class userRegisterView(APIView):
    def post(self,request):
        try:
            data=request.data
            user=User.objects.create(username=data.get("name"),email=data.get("email"))
            user.set_password(data.get("password"))
            user.save()

            refresh = RefreshToken.for_user(user)

            res= {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id
            }
            return Response(res,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class userLoginView(APIView):
    def post(self,request):
        data=request.data
        try:
            user=User.objects.get(email=data.get("email"))
        except:
            user=None
        if user!=None and user.check_password(data.get("password")):
            refresh = RefreshToken.for_user(user)

            res= {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id
            }
            return Response(res,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AdvisorListView(APIView):
    def get(self,request,userid):
        advisor=Advisor.objects.all()
        serializer=AdvisorSerializer(advisor,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AdvisorBookingView(APIView):
    def post(self,request,userid,advisorid):
        try:
            data=request.data
            user=User.objects.get(id=userid)
            advisor=Advisor.objects.get(id=advisorid)
            booking=Booking.objects.create(user=user,advisor=advisor,time=data.get("datetime"))
            booking.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class userBookingDetails(APIView):
    def get(self,request,userid):
        user=User.objects.get(id=userid)
        booking=Booking.objects.filter(user=user)
        res_array=[]
        for each in booking:
            data={}
            serializer=AdvisorSerializer(each.advisor)
            data.update(serializer.data)
            serializer=BookingSerializer(each)
            data.update(serializer.data)
            res_array.append(data)
        return Response(res_array,status=status.HTTP_200_OK)