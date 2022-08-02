import ssl
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_

# ishlagan algoritmlar'AES256-SHA256', 'AES256-SHA', 'CAMELLIA256-SHA', 'AES128-GCM-SHA256', 'AES128-SHA256', 'AES128-SHA', 'CAMELLIA128-SHA'
CIPHERS = (
    'AES256-SHA'
)


class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args,
                                       ssl_context=ctx,
                                       **pool_kwargs)


session = requests.session()
adapter = TlsAdapter(ssl.OP_NO_SSLv2)
session.mount("https://", adapter)
url = 'https://api.smsfly.uz/'
credentials = {
    "key": "8f527b2c-e8d7-11ec-a71e-0242ac120002",
    "phone": "998974251244",
    "message": "test"
}

try:
    response = session.request(method='POST', url=url, json=credentials)
    print(response.text)
except Exception as exception:
    print(exception)