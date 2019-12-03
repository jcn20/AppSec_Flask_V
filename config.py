import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
APP_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_PATH = os.path.join(ROOT_PATH, 'static')
TEMPLATES_PATH = os.path.join(ROOT_PATH, 'templates')
WORDLIST_FILE = os.path.join(ROOT_PATH, 'wordlist.txt')
