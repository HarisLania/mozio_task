from django.test import TestCase
from provider.models import Provider
from service_area.models import ServiceArea
from rest_framework.test import RequestsClient

class ProviderTestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.provider = Provider.objects.create(name='test1', 
                                                phone_number='12356', 
                                                email='test1@email.com',
                                                language='urdu',
                                                currency='usd'
                                                )
        cls.service_area = ServiceArea.objects.create(
                                                    name='test_area',
                                                    price=123,
                                                    long=123.23,
                                                    lat=12.32,
                                                    provider=cls.provider
                                                )

    def test_get_method(self):
        """
        GET method test service-area
        """
        client = RequestsClient()
        retrieve_response = client.get('http://127.0.0.1:8000/service-area/'
                            +str(self.service_area.id)
                            )
        list_response = client.get('http://127.0.0.1:8000/service-area/')
        assert (retrieve_response.status_code == 200 and list_response.status_code == 200)
    

    def test_post_method(self):
        """
        POST method test service-area
        """
        client = RequestsClient()
        response = client.post('http://127.0.0.1:8000/service-area/', data={
                                                                        "name":'test_area_new',
                                                                        "price":123,
                                                                        "long":123.23,
                                                                        "lat":12.32,
                                                                        "provider":self.provider.id
                                                                    })
        assert response.status_code == 200
    

    def test_put_method(self):
        """
        PUT method test service-area
        """
        client = RequestsClient()
        response = client.put('http://127.0.0.1:8000/service-area/'
                                +str(self.service_area.id), data={
                                                            "name":'test_area_put',
                                                            "price":123,
                                                            "long":123.23,
                                                            "lat":12.32,
                                                            "provider":self.provider.id
                                                        })
        assert response.status_code == 200
    
    def test_patch_method(self):
        """
        PATCH method test service-area
        """
        client = RequestsClient()
        response = client.patch('http://127.0.0.1:8000/service-area/'
                                +str(self.service_area.id), data={
                                                            'name':'test_area_patch',
                                                        })
        assert response.status_code == 200
    
    def test_delete_method(self):
        """
        DELETE method test service-area
        """
        client = RequestsClient()
        response = client.delete('http://127.0.0.1:8000/service-area/'+str(self.service_area.id))
        assert response.status_code == 204

    
    def test_polygon_endpoint(self):
        """
        Polygon endpoint (input: lat,long)
        """
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/service-area/85.42000/182.20000')
        assert response.status_code == 200