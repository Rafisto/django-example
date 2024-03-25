from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.menu1 = MenuItem.objects.create(Title='Menu 1', Price=10.99, Inventory=100)
        self.menu2 = MenuItem.objects.create(Title='Menu 2', Price=12.99, Inventory=100)
        self.client = APIClient()
        self.client.login(username='testuser', password='12345')

    def test_get_all(self):
        url = reverse('menu-items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        serialized_data = MenuItemSerializer([self.menu1, self.menu2], many=True).data
        self.assertEqual(response.data, serialized_data)
