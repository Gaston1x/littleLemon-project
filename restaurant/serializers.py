from rest_framework import serializers 
from .models import Menu, Booking
from rest_framework.validators import UniqueTogetherValidator 
from django.contrib.auth.models import User 
 
class BookingSerializer (serializers.ModelSerializer): 
    class Meta:
        model = Booking
        fields = ['id','name','no_of_guests','bookingdate']
        validators = [
        ]

class MenuSerializer (serializers.ModelSerializer): 

    class Meta:
        model = Menu
        fields = ['id','title','price','inventory']
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


# class CartSerializer (serializers.ModelSerializer): 
#     user = serializers.PrimaryKeyRelatedField( 
#     queryset=User.objects.all(), 
#     default=serializers.CurrentUserDefault() 
#     ) 
#     class Meta:
#         model = Cart
#         fields = ['user','menuitem','quantity', 'price']
#         extra_kwargs = {
#             'quantity': {'min_value': 0},
#         }



# class OrderSerializer (serializers.ModelSerializer): 
#     user = serializers.PrimaryKeyRelatedField( 
#     queryset=User.objects.all(), 
#     default=serializers.CurrentUserDefault() 
#     ) 
#     class Meta:
#         model = Order
#         fields = ['id','user','delivery_crew','status', 'total', 'date']


# class OrderItemSerializer (serializers.ModelSerializer): 

#     class Meta:
#         model = OrderItem
#         fields = ['order','menuitem','quantity', 'unit_price', 'price']

#         extra_kwargs = {
#             'quantity': {'min_value': 0},
#         }

# class ManagerSerializer (serializers.ModelSerializer): 
#     class Meta:
#         model = User
#         fields = ['id','username','email']

# class DeliveryCrewSerializer (serializers.ModelSerializer): 
#     class Meta:
#         model = User
#         fields = ['id','username','email']