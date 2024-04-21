# buyer request
import requests

session = requests.session()

burp0_url = "https://chat.ghtk.vn:443/api/v31/channels/direct?partner_id=buyer_84335608482"
burp0_headers = {"Apptype": "iGHTK_iOS", "Content-Type": "application/json", "Accept": "application/json", "Authorization": "Bearer c_agamsdlvkltfvrarahadme1pwchy695m2yymoxfbxaf1hfwvpjv3bkip1tuqgluo", "Appversion": "1.3.23", "Accept-Language": "vi-VN;q=1.0", "Accept-Encoding": "gzip, deflate, br", "Ismobileapp": "1", "Devicetoken": "136873df64c3566e2789e0b54b147dcb40d0f53bc05126bb0b17f2070bd233a4", "Deviceid": "F817D115-5BF7-4013-912F-D8A8700F9948", "User-Agent": "iGHTK/1.3.23 (com.ightk.ez; build:1; iOS 17.4.1) Alamofire/4.9.1", "Device_id": "433867A7-795D-42B5-A6FA-7D646D4AA673", "Devicetokenmpc2c": "136873df64c3566e2789e0b54b147dcb40d0f53bc05126bb0b17f2070bd233a4", "Device": "ios"}
session.get(burp0_url, headers=burp0_headers)

# get user info by user_key

import requests

session = requests.session()

burp0_url = "https://chat.ghtk.vn:443/api/v3/users?user_key=buyer_84989755968"
burp0_headers = {"Content-Type": "application/json", "Apptype": "iGHTK_iOS", "Accept": "application/json", "Authorization": "Bearer c_agamsdlvkltfvrarahadme1pwchy695m2yymoxfbxaf1hfwvpjv3bkip1tuqgluo", "Appversion": "1.3.23", "Accept-Language": "vi-VN;q=1.0", "Accept-Encoding": "gzip, deflate, br", "Ismobileapp": "1", "Devicetoken": "136873df64c3566e2789e0b54b147dcb40d0f53bc05126bb0b17f2070bd233a4", "Deviceid": "F817D115-5BF7-4013-912F-D8A8700F9948", "User-Agent": "iGHTK/1.3.23 (com.ightk.ez; build:1; iOS 17.4.1) Alamofire/4.9.1", "Device_id": "433867A7-795D-42B5-A6FA-7D646D4AA673", "Devicetokenmpc2c": "136873df64c3566e2789e0b54b147dcb40d0f53bc05126bb0b17f2070bd233a4", "Device": "ios"}
session.get(burp0_url, headers=burp0_headers)