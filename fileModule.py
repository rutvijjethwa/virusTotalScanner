import requests
import os.path as op
from pprint import pprint


def fileScanner(fileLocation, publicKey):
    """
    Description For This Module
    NOTE : Add Absolute path
    :return:
    """

    fileToScan = {'file':(op.split(fileLocation)[1], open(fileLocation, 'rb'))}
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=fileToScan, params=publicKey)
    json_response = response.json()
    pprint(json_response)
    return json_response.get('resource')


if __name__ == '__name__':
    pass
