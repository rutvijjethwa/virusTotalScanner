# virusTotalScanner

vScan is a tool to scan for and website for malware or any such entity using python puiblic API of Virus Total.

This script is for educational purpose only.

You need to add your own API key for running this virusTotalScanner in "cofig.ini" file.

To get the API Key, Sign up to VirusTotal Community. Once you have a valid VirusTotal Community account,
you will find your personal API key in your Community profile. This key is all you need to use VirusTotal's API.

#####################################################################################################

The public API is a free service, available for any website or application that is free to consumers. 
The API must not be used in commercial products or services, it can not be used as a substitute for
antivirus products and it can not be integrated in any project that may harm the antivirus industry
directly or indirectly. 
Noncompliance of these terms will result in immediate permanent ban of the infractor individual or
organization.Please see the terms of service for more information.

####################################################################################################

NOTE:Please Refer https://www.virustotal.com/about/terms-of-service/

______________________________________________________________________________________________________
To scan a file use '-f'

STNTAX:

python vScan.py -f <Absolute-filepath>
        
        Note: Use absoulte path

EXAMPLE:

         python vScan.py -f C:/Users/ABC/Desktop/data/file_to_be_scanned.txt

______________________________________________________________________________________________________
To scan a url use '-u'

SYNTAX:

         python vScan.py -u <url>

EXAMPLE:

         python vScan.py -u http://www.example.com

______________________________________________________________________________________________________
