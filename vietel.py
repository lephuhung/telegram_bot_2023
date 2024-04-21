# find sdt, cccd, account
import requests

session = requests.session()

burp0_url = "https://apigami.viettel.vn:443/mvt-api/myviettel.php/contractListByContactPhoneV2"
burp0_headers = {"Accept": "*/*", "App_version": "7.7", "Content-Type": "application/x-www-form-urlencoded", "Device_id": "DED91FFF-7670-4BA0-8DD6-3E516BF7F64B", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "MyViettel/7.7 (iPad; iOS 17.4.1; Scale/2.00)", "Accept-Language": "vi-VN;q=1", "Connection": "close"}
burp0_data = {"build_code": "2024.3.20", "device_id": "DED91FFF-7670-4BA0-8DD6-3E516BF7F64B", "device_name": "iPad (iPad14,1)", "isdn": "184144787", "myvt_checksum": "mYddSdwgOj7RHuLgiBh8bzo+vik=", "os_type": "ios", "os_version": "17.400000", "token": "4df773f8-7bb7-432e-afbb-75b626deafd8-aDAzOV9nZnR0aF9odW5nbHA1", "type": "1", "version_app": "7.7"}
session.post(burp0_url, headers=burp0_headers, data=burp0_data)


# modem info
import requests

session = requests.session()

burp0_url = "https://apigami.viettel.vn:443/mvt-api/myviettel.php/modem/info"
burp0_headers = {"Content-Type": "multipart/form-data; boundary=Boundary+5C4AA8C7445CF43E", "Accept": "*/*", "App_version": "7.7", "Upload-Incomplete": "?0", "Upload-Draft-Interop-Version": "3", "Accept-Language": "vi-VN;q=1", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "MyViettel/7.7 (iPad; iOS 17.4.1; Scale/2.00)", "Device_id": "DED91FFF-7670-4BA0-8DD6-3E516BF7F64B", "Connection": "close"}
burp0_data = "--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"build_code\"\r\n\r\n2024.3.20\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"deviceBandType\"\r\n\r\n2\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"deviceMac\"\r\n\r\n90:fd:73:d7:38:d7\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"device_id\"\r\n\r\nDED91FFF-7670-4BA0-8DD6-3E516BF7F64B\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"device_name\"\r\n\r\niPad (iPad14,1)\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"hangSX\"\r\n\r\nZTE\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"myvt_checksum\"\r\n\r\nmYddSdwgOj7RHuLgiBh8bzo+vik=\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"os_type\"\r\n\r\nios\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"os_version\"\r\n\r\n17.400000\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"serial\"\r\n\r\nZTEEH7VL9210664\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\n4df773f8-7bb7-432e-afbb-75b626deafd8-aDAzOV9nZnR0aF9odW5nbHA1\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"version_app\"\r\n\r\n7.7\r\n--Boundary+5C4AA8C7445CF43E\r\nContent-Disposition: form-data; name=\"logsFile\"; filename=\"h039_gftth_hunglp5.txt\"\r\nContent-Type: text/plain\r\n\r\n\r\n--Boundary+5C4AA8C7445CF43E--\r\n"
session.post(burp0_url, headers=burp0_headers, data=burp0_data)