import requests
from pprint import pprint


def urlScanner(targeturl, keyString):
    """
    Discription For This Module
    :return:
    """
    dataSet = {'apikey': keyString, 'url': targeturl}
    response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=dataSet)
    json_response = response.json()
    pprint(json_response)
    return json_response.get('url')

if __name__ == '__main__':
    pass
