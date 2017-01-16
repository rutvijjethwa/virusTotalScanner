import requests
import os.path
import time
import pandas as pd

def getReportf(publicKey, resourceID,filename):
    dataSet = {'apikey': publicKey, 'resource': resourceID}
    reportHeaders = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "gzip,  Holly Mother Of Godzilla"
    }
    while True:
        try:
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=dataSet, headers=reportHeaders)
            json_response = response.json()
            if json_response.get('verbose_msg') == 'Scan finished, information embedded':
                break
            else:
                time.sleep(10)
        except:
            continue
    print("####################################################")
    fname = os.path.basename(filename)
    df = pd.DataFrame(json_response)
    writer = pd.ExcelWriter('{}_report.xlsx'.format(fname))
    df.to_excel(writer)
    writer.save()
    print('Report Saved to : {}'.format(os.getcwd()))


def getReportu(publicKey, resourceID,filename):
    reportHeaders = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "gzip,  Holly Mother Of Godzilla"
    }
    dataSet = {'apikey': publicKey, 'resource': resourceID}
    response = requests.post('https://www.virustotal.com/vtapi/v2/url/report', params=dataSet, headers=reportHeaders)
    json_response = response.json()
    print("####################################################")
    df = pd.DataFrame(json_response)
    writer = pd.ExcelWriter('Website_report.xlsx')
    df.to_excel(writer)
    writer.save()
    print('Report of website {} is Saved at : {}'.format(filename,os.getcwd()))
