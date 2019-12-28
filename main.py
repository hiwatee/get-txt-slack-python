import os
from os.path import join, dirname
from dotenv import load_dotenv


def main():
    # .envから環境変数を読み込み
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    TOKEN = os.environ.get("TOKEN")


if __name__ == '__main__':
    main()
