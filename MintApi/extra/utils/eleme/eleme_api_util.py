import hashlib
import urllib
from cgi import FieldStorage

def concat_params(params):
    pairs = []
    for key in sorted(params):
        if key == 'sig':
            continue
        val = params[key]
        if isinstance(val, unicode):
            val = urllib.quote_plus(val.encode('utf-8'))
        elif isinstance(val, str):
            val = urllib.quote_plus(val)
        if not isinstance(val, FieldStorage):
            pairs.append("{}={}".format(key, val))
    return '&'.join(pairs)


def gen_sig(path_url, params, consumer_secret):
    params = concat_params(params)

    to_hash = u'{}?{}{}'.format(
        path_url, params, consumer_secret
    ).encode('utf-8').encode('hex')

    sig = hashlib.new('sha1', to_hash).hexdigest()
    return sig