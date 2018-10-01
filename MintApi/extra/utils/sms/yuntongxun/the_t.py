import base64

YTX_SMS = {
    'SMS_BASE_URL': 'https://app.cloopen.com:8883',
    'SMS_PARAM_URL': '/2013-12-26/Accounts/{}/SMS/TemplateSMS?sig={}',

    'SMS_APP_ID': '8aaf070866235bc501662d56671a0776',
    'SMS_ACCOUNT_ID': '8aaf070866235bc501662d5666b70770',
    'SMS_TEMPLATE_ID': 1,

    'SMS_APP_TOKEN': 'd918a344f57f4929a0d41266e242c631'
}

def base64_test():
    a = 'i love you'.encode(encoding='utf-8')
    print(type(a), ' : ', a)

def dict_items_test():
    a = [v for k,v in YTX_SMS.items()]
    print(a)
    print(type(a))

# dict_items_test()

a = '80DW'.lower()
print(a)