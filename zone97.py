import requests

session = requests.session()

burp0_url = "http://api.zone97.vn:80/user/login-telco"
burp0_headers = {"Accept": "*/*", "Authorization": "Bearer", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "vi-VN,vi;q=0.9", "X-Zone97-Api-Key": "cb62ecc101f2cabe23", "Origin": "http://zone97.vn", "Connection": "close", "User-Agent": "Mozilla/5.0 (iPad; CPU OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1", "Referer": "http://zone97.vn/"}
session.post(burp0_url, headers=burp0_headers)