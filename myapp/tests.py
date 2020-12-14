from django.test import TestCase
from myapp.models import Device

class AnimalTestCase(TestCase):
    def setUp(self):
        device = Device(address="lion")
        device.save()
        # Animal.objects.create(name="cat", sound="meow")

    # def test_animals_can_speak(self):
    #     """Animals that can speak are correctly identified"""
    #     lion = Animal.objects.get(name="lion")
    #     cat = Animal.objects.get(name="cat")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')