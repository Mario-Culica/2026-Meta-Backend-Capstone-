from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuTest(TestCase):
    def test_str_representation(self):
        menu_item = Menu.objects.create(
            title="IceCream",
            price=80.00,
            inventory=100
        )
        self.assertEqual(str(menu_item), "IceCream")


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(
            title="IceCream",
            price=80.00,
            inventory=100
        )
        Menu.objects.create(
            title="Pasta",
            price=150.00,
            inventory=50
        )

    def test_getall(self):
        client = APIClient()
        response = client.get("/restaurant/menu/items")

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
