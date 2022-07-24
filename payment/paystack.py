from django.conf import settings
import requests


class Paystack:
    PAYSTACK_SECRET_KEY = 'sk_test_b70fe78f55470d7da98c8f9af34bc601cd43d9cb'
    base_url ='http://api.paystack.co'

    def verify_payment(self, ref, *args, **kwargs):
        path = f'/transaction/verify/{ref}'
        PAYSTACK_SECRET_KEY = 'sk_test_b70fe78f55470d7da98c8f9af34bc601cd43d9cb'
        base_url ='http://api.paystack.co'

        headers={
            "Authorization": f"Bearer{PAYSTACK_SECRET_KEY}",
            'Contect-Type' :'application/json',
        }

        url= base_url + path
        
        response = requests.get(url, headers )

        if response.status_code == 200:
            response_data =response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data["status"], response_data["message"]
