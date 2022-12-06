proxy_servers = {
    'http': 'http://103.207.8.130:23804',
    'https': 'https://103.207.8.130:23804'
}




import requests

url = "http://example.com"

header = requests.utils.default_headers()
header.update={"User-Agent":"#user agent of your system  "}

http_proxy = "104.16.107.38:80"
proxy_servers = {
    'http': "http://" + http_proxy,
    'https': "https://" + http_proxy
}

page = requests.get(url,timeout= 5, headers=header, proxies=proxy_servers)