import requests
from MintApi import settings

class AddrBaidu(object):
    url = settings.BAIDU_MAP_LOCATION_URL
    def __init__(self, location, ak=settings.BAIDU_MAP_AK, output='json'):
        self.ak = ak
        self.location = location
        self.output = output

    def _get_online_result(self, url, params):
        ret = requests.get(url = url, params = params)
        return ret.json()

    def get_addr_dict(self):
        params = {
            'location': self.location,
            'output': self.output,
            'ak': self.ak
        }
        addr_json = self._get_online_result(self.url, params)
        if addr_json['status'] != 0:
            raise Exception('Get Location Error, {code}: {msg}'.format(code = addr_json['status'], msg = addr_json['msg']))
        else:
            return addr_json['result']