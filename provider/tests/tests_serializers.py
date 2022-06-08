from django.test import TestCase
from provider.models import Provider
from service_area.models import ServiceArea
from rest_framework.test import RequestsClient

class ProviderTestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.provider = Provider.objects.create(name='test1', 
                                                phone_number='12356', 
                                                email='test1@email.com',
                                                language='urdu',
                                                currency='usd'
                                                )
        cls.service_area = ServiceArea.objects.create(name='test_area',
                                                        price=123,
                                                        long=123.23,
                                                        lat=12.32,
                                                        provider=cls.provider
                                                    )
        
    def test_to_representation(self):
        """
        Checking if foreign key diplaying complete data
        """
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/service-area/'
                            +str(self.service_area.id))
        assert response.status_code == 200
    

    def test_to_internal(self):
        """
        Checking if need to add the foreign key id only
        """
        client = RequestsClient()
        response = client.post('http://127.0.0.1:8000/service-area/', 
                                data={
                                    'name':'test_area1',
                                    'price':123,
                                    'long':'182.123',
                                    'lat': '23.23',
                                    'provider':1
                                })
        assert response.status_code == 200