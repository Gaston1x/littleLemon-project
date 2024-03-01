from .test_models import MenuTest
from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User 

class MenuViewTest (TestCase):
    def setup(self):
        item1 = Menu.objects.create(title="Chocolate", price=5, inventory=20)
        item2 = Menu.objects.create(title="Steak", price=50, inventory=40)

    def test_getall(self):
        #some reason the setup is ignored
        item1 = Menu.objects.create(title="Cake", price=5, inventory=30)
        item2 = Menu.objects.create(title="Else", price=50, inventory=20)
        c = Client()
        user = User.objects.create_user(username='test',password='test@123')
        c.force_login(user)
        serializer = MenuSerializer(Menu.objects.all(), many = True)
        response = c.get("/restaurant/menu/")
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
    

        