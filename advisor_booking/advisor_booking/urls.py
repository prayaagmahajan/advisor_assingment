"""advisor_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from advisor.views import advisorView,bookingView,AdvisorView,userRegisterView,userLoginView,AdvisorListView,AdvisorBookingView,userBookingDetails
# Create a router and register our viewsets with it.


router = DefaultRouter()
# router.register(r'admin/advisor', advisorView)
router.register(r'booking',bookingView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('advisor/',AdvisorView.as_view(),name="advisor"),
    path('user/register/',userRegisterView.as_view(),name="user-register"),
    path('user/login/',userLoginView.as_view(),name="user-login"),
    path('user/<int:userid>/advisor/',AdvisorListView.as_view(),name="advisor-list"),
    path('user/<int:userid>/advisor/<int:advisorid>/',AdvisorBookingView.as_view(),name="advisor-booking-view"),
    path('user/<int:userid>/advisor/booking/',userBookingDetails.as_view(),name="user-booking-details-view")
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)