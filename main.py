import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv
# from pprint import pprint


def main():
    # .envから環境変数を読み込み
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    token = os.environ.get("TOKEN")
    host = os.environ.get("HOST")
    # チャンネルリストを取得・整形
    url = host + 'channels.list?token=' + token + '&exclude_archived=true'
    r = requests.get(url)
    data = r.json()
    channels = [{'id': channel['id'], 'name': channel['name']}
                for channel in data['channels']]
    for channel in channels:
        url = host + 'channels.history?token=' + \
            token + '&channel=' + channel['id'] + '&count=1000'
        r = requests.get(url)
        data = r.json()
        with open(dirname(__file__) + 'output.txt', 'a') as f:
            for message in data['messages']:
                print(message['text'], file=f)
    # 各チャンネルから上位1000件を取得する


if __name__ == '__main__':
    main()
