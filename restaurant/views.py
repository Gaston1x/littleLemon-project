from django.shortcuts import render
from .models import Menu, Booking
from rest_framework import generics, status, viewsets
# from rest_framework.viewsets import ModelViewSet 
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User 

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # ordering_fields = ['price', 'title']
    # search_fields = ['title']

    # def get_permissions(self):
    #     checkpermissions = []
    #     if(self.request.method=='GET'):
    #         checkpermissions = [IsAuthenticated]
    #     elif self.request.method == 'POST':
    #         checkpermissions = [IsAuthenticated , ManagerAccess |IsAdminUser]
    #     return [permission() for permission in checkpermissions]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # def get_permissions(self):
    #     checkpermissions = [IsAuthenticated , ManagerAccess | IsAdminUser]
    #     return [permission() for permission in checkpermissions]

class BookingViewSet (viewsets.ModelViewSet):
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     checkpermissions = [IsAuthenticated , ManagerAccess | IsAdminUser]
    #     return [permission() for permission in checkpermissions]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]