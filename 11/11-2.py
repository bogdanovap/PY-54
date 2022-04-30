import os
import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.host = "https://cloud-api.yandex.net:443"

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        file_name = os.path.basename(file_path)
        headers = {
            "Accept": "application/json",
            "Authorization": f"OAuth {self.token}"
        }
        parameters = {"path": f"{file_name}",
                      "overwrite": "true"
        }

        res = requests.get(f"{self.host}/v1/disk/resources/upload", headers=headers, params=parameters)
        print(res)
        link = res.json()["href"]
        parameters["url"] = link

        res = requests.put(link, data=open(file_path, "rb"), headers=headers, params=parameters)
        print(res)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "test.txt"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)