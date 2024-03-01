from .test_models import MenuTest
from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.views import MenuItemsView
from django.contrib.auth.models import User 

class MenuViewTest (TestCase):
    def setup(self):
        Menu.objects.create(title="Chocolate", price=5, inventory=20)
        Menu.objects.create(title="Steak", price=50, inventory=40)
    def test_getall(self):
        c = Client()
        user = User.objects.create_user(username='test',password='test@123')
        c.force_login(user)
        response = c.get("/restaurant/menu/")
        self.assertEqual(response.data, Menu.objects.all())
    

        