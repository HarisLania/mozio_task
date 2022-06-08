from django.test import TestCase
from service_area.models import ServiceArea
from provider.models import Provider

class ServiceAreaTestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        provider = Provider.objects.create(name='test1', 
                                    phone_number='12356', 
                                    email='test1@email.com',
                                    language='urdu',
                                    currency='usd'
                                    )
        cls.service_area = ServiceArea.objects.create(name='test_area',
                                                    price=123,
                                                    long=123.23,
                                                    lat=12.32,
                                                    provider=provider
                                                    )
        
    def test_service_area_str(self):
        """
        Checking __str__ method of model class ServiceArea
        """
        self.assertEqual(str(self.service_area), 'test_area | Location: (12.32,123.23)')
    
    def test_cordinates(self):
        self.assertEqual(self.service_area.cordinates, (12.32,123.23))