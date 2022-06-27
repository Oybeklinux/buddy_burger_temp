import json
import random
import environ
import requests
import ssl
from urllib3 import poolmanager

env = environ.Env()
environ.Env.read_env()


class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)


def send_otp_to_phone(phone_number):
    try:
        otp = random.randint(100000, 999999)
        url = 'https://api.smsfly.uz/'
        credentials = {
            "key": env("token"),
            "phone": str(phone_number),
            "message": str(otp)
        }
        session = requests.session()
        session.mount('https://', TLSAdapter())
        res = session.post(url=url, json=credentials)
        data = json.loads(res.text)
        if data['success']:
            return otp

        print("Kutilmagan xatolik")
        return None
    except Exception as e:
        print(e)
    return None
