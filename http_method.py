
import import_file as f
import requests

def post(url,query_args):
    x = requests.post(url, data = query_args)
    return x.text
