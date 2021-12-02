import os
import requests
import config


def get_data(data_file, input_url):
    if not os.path.exists(data_file):
        cookies = dict(session=config.session_cookie)
        r = requests.get(input_url, cookies=cookies)
        with open(data_file, 'w+') as file:
            file.write(r.text)
