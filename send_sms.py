import requests
import ssl
from urllib3 import poolmanager
import json

url = 'https://api.smsfly.uz/'
credentials = {
	"key": "8f527b2c-e8d7-11ec-a71e-0242ac120002",
	"phone": "998974251244",
	"message": "test"
}


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


session = requests.session()
session.mount('https://', TLSAdapter())
res = session.post(url=url,json=credentials)
print(res.text)
data = json.loads(res.text)
print(data['success'])