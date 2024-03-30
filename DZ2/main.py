import unittest
import requests
import json

BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources/'
# токен Яндекса
token = ''
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'OAuth {token}'
            }
def create_folder(path):
        params={'path': path}
        response = requests.put(BASE_URL, headers=headers, params=params)
        return response


class YANDEXAPIClient:
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'OAuth y0_AgAAAAABnMNfAAq0uAAAAADv9DRBiy5mUYgHS5qp_p4rRHetJ5anXJI'
            }
    def __init__(self, token):
        token = token
        self.headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'OAuth {token}'
                    }
    
    def create_folder(self,path):
        params={'path': path}
        response = requests.put(self.BASE_URL, headers=self.headers, params=params)
        # print(response.headers)
        # print()
        # print(response.content)
        # print()
        # print(response.status_code)
        return response
    

    def upload_files(self, file, file_url):
        # payload = {}
        params={'path': file,
                'url': file_url
              }
        url = f"{self.BASE_URL}upload"
        response = requests.request("POST", url, headers=self.headers, params=params)
        return response.status_code

class Test_yandex_api(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.path1 = 'test'
        self.path2 = '123'
        self.path3 = 'тест'
        self.path4 = '_test'
        self.path5 = 'test.py'
        super().__init__(methodName)
    def setUp(self) -> None:
        # self.path1 = 'test'
        # self.path2 = '123'
        # self.path3 = 'тест'
        # self.path4 = '_test'
        # self.path5 = 'test.py'
        return super().setUp()
    def test_yandex_create_folder1(self):
        code=201
        self.assertEqual(create_folder(self.path1).status_code,code)
    def test_yandex_create_folder2(self):
        code=201
        self.assertEqual(create_folder(self.path2).status_code,code)
    def test_yandex_create_folder3(self):
        code=201
        self.assertEqual(create_folder(self.path3).status_code,code)
    def test_yandex_create_folder4(self):
        code=201
        self.assertEqual(create_folder(self.path4).status_code,code)
    def test_yandex_create_folder5(self):
        code=201
        self.assertEqual(create_folder(self.path5).status_code,code)


    def tearDown(self) -> None:
        # if AssertionError:
        #     print("number error", AssertionError.args)
        # response = create_folder(path)
        # json_data = json.loads(response.content.decode('utf-8'))
        # if int(response.status_code) > 202:
        #     print(json_data['message'])
        # else:
        #     print("OK")
        # print('asd')
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()


