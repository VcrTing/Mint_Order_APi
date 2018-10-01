
import time
import base64
import hashlib

import requests

__author__ = 'VcrTing'

# setting_dict 配置示例:
YTX_SMS = {
    'SMS_BASE_URL': 'https://app.cloopen.com:8883',
    'SMS_PARAM_URL': '/2013-12-26/Accounts/{}/SMS/TemplateSMS?sig={}',
    'SMS_APP_ID': '8aaf070866235bc501662d56671a0776',
    'SMS_APP_TOKEN': 'd918a344f57f4929a0d41266e242c631',
    'SMS_ACCOUNT_ID': '8aaf070866235bc501662d5666b70770',
    'SMS_TEMPLATE_ID': 1
}

class YTXJsonSms():

    the_time = time.strftime("%Y%m%d%H%M%S", time.localtime())

    def __init__(self, setting_dict):
        setting_list = [v for k,v in setting_dict.items()]
        self.BASE_URL = setting_list[0]
        self.PARAM_URL = setting_list[1]
        self.account_id = setting_list[2]
        self.auth_token_id = setting_list[3]
        self.app_id = setting_list[4]
        self.template_id = setting_list[5]

    def _get_sig(self):
        ret = self.account_id + self.auth_token_id + self.the_time
        mdf = hashlib.md5()
        mdf.update(ret.encode(encoding='utf-8'))
        ret = mdf.hexdigest()
        return ret.upper()

    def _get_authorization(self):
        ret = self.account_id + ':' + self.the_time
        ret = base64.b64encode(ret.encode(encoding='utf-8'))
        return ret

    def get_url(self):
        sig = self._get_sig()
        ret = self.BASE_URL + self.PARAM_URL.format(self.account_id, sig)
        return ret

    def get_header(self):
        authorization = self._get_authorization()
        ret = {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': authorization
        }
        return ret

    def get_params(self, phone_list, data_list):
        ret = {
            'to': ','.join(phone_list),
            'appId': self.app_id,
            'templateId': str(self.template_id),
            'datas': data_list
        }
        return ret

    def request_sms(self, phone_list, data_list):
        url = self.get_url()
        headers = self.get_header()
        params = self.get_params(phone_list, data_list)
        response = requests.post(url=url, data=params, headers=headers)
        print(response)

if __name__ == '__main__':
    s = YTXJsonSms(YTX_SMS)
    phone_list = ['13576639986']
    data_list = ['6358', '30s']
    s.request_sms(phone_list, data_list)