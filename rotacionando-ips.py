import urllib3
import random

# Proxies retirados de https://free-proxy-list.net
# Depois tentar obter os ips dinamicamente através de scraping.
proxies = [
    'https://91.211.189.106:8080',
    'https://83.215.247.182:53281'
]

def retornaIpProxy():
    return random.choice(proxies)


if "__main__" == __name__:
    import certifi
    url = 'https://httpbin.org/ip'
    proxy = urllib3.ProxyManager(retornaIpProxy(),cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    req = proxy.request('GET', url)
    print(req.data)
