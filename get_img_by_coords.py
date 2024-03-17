from config import STATIC_API_KEY
import requests
import sys
import os

second_coord, first_coord = 47.237191, 39.611298


def get_img(second_coord, first_coord):
    map_request = f'http://static-maps.yandex.ru/1.x/?ll={first_coord},{second_coord}&spn=0.002,0.002&l=map'
    response = requests.get(map_request)

    map_file = "map_img.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    if not response:
        print(f"Ошибка выполнения запроса:{map_request}; \n Http статус: {response.status_code};")
        sys.exit(1)


get_img(47.237191, 39.611298)
