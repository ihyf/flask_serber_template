import time
import json
import requests
import base64


class Hyf(object):
    def __init__(self):
        self.appid = "hyf_app"
        self.headers = {
            "content-type": "application/json",
            "Authorization": "json rpc test"
        }
        self.payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "",
            "params": {

            }
        }
        self.url_local = "http://localhost:9000/api"
        self.url_wai = "http://xx.xx.xx.xx:9000/api"
    
    def send_request(self, url, method, data):
        self.payload["method"] = method
        self.payload["params"] = data
        print(url)
        print(self.payload)
        response = requests.post(url=url, data=json.dumps(self.payload), headers=self.headers)
        print(response.json())

    def test_hello(self):
        method = "hello"
        data = {
            "time": time.time()
        }
        self.send_request(url=self.url_local, method=method, data=data)


if __name__ == "__main__":
    hyf = Hyf()
    hyf.test_hello()


