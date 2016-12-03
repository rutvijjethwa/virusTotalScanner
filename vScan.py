import sys
from configparser import ConfigParser
from fileModule import fileScanner
from urlModule import urlScanner
import report

configReader = ConfigParser()
configReader.read(filenames='config.ini')
key = {'apikey': configReader['API']['apikey']}

if sys.argv[1] == '-h':
    print("""
         vScan is a tool to scan for and website for malware or any such entity.
         To scan a file use '-f'
         eg: python vScan.py -f <Absolute-filepath>
         Note: Use absoulte path

         To scan a url use '-u'
         eg: python vScan.py -u <url>
    """ )
elif sys.argv[1] == '-f':
    reportID = fileScanner(fileLocation=sys.argv[2], publicKey=key)
    report.getReportf(key.get('apikey'), reportID)
elif sys.argv[1] == '-u':
    reportID = urlScanner(sys.argv[2], key.get('apikey'))
    report.getReportu(key.get('apikey'), reportID)
else:
    print("INVALID INPUT")
