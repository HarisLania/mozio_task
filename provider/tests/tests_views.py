from django.test import TestCase
from provider.models import Provider
from service_area.models import ServiceArea
from rest_framework.test import RequestsClient
from http import HTTPStatus

class ProviderTestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.provider = Provider.objects.create(name='test1', 
                                    phone_number='12356', 
                                    email='test1@email.com',
                                    language='urdu',
                                    currency='usd'
                                    )

    def test_get_method(self):
        """
        GET method test provider
        """
        client = RequestsClient()
        retrieve_response = client.get('http://127.0.0.1:8000/provider/'
                            +str(self.provider.id)
                            )
        list_response = client.get('http://127.0.0.1:8000/provider/')
        assert (retrieve_response.status_code == 200 and list_response.status_code == 200)
    

    def test_post_method(self):
        """
        POST method test provider
        """
        client = RequestsClient()
        response = client.post('http://127.0.0.1:8000/provider/', data={
                                                                        'name':'test',
                                                                        'phone_number':"12345",
                                                                        'email':'test@email.com',
                                                                        'language': 'urdu',
                                                                        'currency':'pkr'
                                                                    })
        self.assertEqual(response.status_code, HTTPStatus.CREATED._value_)
    

    def test_put_method(self):
        """
        PUT method test provider
        """
        client = RequestsClient()
        response = client.put('http://127.0.0.1:8000/provider/'
                                +str(self.provider.id), data={
                                                            'name':'test_put',
                                                            'phone_number':"1232345",
                                                            'email':'test_put@email.com',
                                                            'language': 'urdu',
                                                            'currency':'pkr'
                                                        })
        self.assertEqual(response.status_code, HTTPStatus.ACCEPTED._value_)
    
    def test_patch_method(self):
        """
        PATCH method test provider
        """
        client = RequestsClient()
        response = client.put('http://127.0.0.1:8000/provider/'
                                +str(self.provider.id), data={
                                                            'name':'test_patch',
                                                        })
        self.assertEqual(response.status_code, HTTPStatus.ACCEPTED._value_)
    
    def test_delete_method(self):
        """
        DELETE method test provider
        """
        client = RequestsClient()
        response = client.delete('http://127.0.0.1:8000/provider/'+str(self.provider.id))
        assert response.status_code == 204