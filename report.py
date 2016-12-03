from pprint import pprint
import requests


def getReportf(publicKey, resourceID):
    dataSet = {'apikey': publicKey, 'resource': resourceID}
    reportHeaders = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "gzip,  Holly Mother Of Godzilla"
    }
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=dataSet, headers=reportHeaders)
    json_response = response.json()
    print("####################################################")
    pprint(json_response)

def getReportu(publicKey, resourceID):
    reportHeaders = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "gzip,  Holly Mother Of Godzilla"
    }
    dataSet = {'apikey': publicKey, 'resource': resourceID}
    response = requests.post('https://www.virustotal.com/vtapi/v2/url/report', params=dataSet, headers=reportHeaders)
    json_response = response.json()
    print("####################################################")
    pprint(json_response)
