from django.test import TestCase
from provider.models import Provider

class ProviderTestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.provider = Provider.objects.create(name='test1',
                                                phone_number='12356', 
                                                email='test1@email.com',
                                                language='urdu',
                                                currency='usd'
                                            )
        
    def test_provider_str(self):
        """
        Checking __str__ method of model class Provider
        """
        self.assertEqual(str(self.provider), 'test1 | 12356')