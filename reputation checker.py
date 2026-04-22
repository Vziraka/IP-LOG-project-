from multiprocessing import Value
from urllib3.util.url import Url
from IP_address_loop import Flagged

import requests 
import json 
import os #gives access to your operating system so it can read your enviromental variables
from dotenv import load_dotenv 


load_dotenv() # this loads the .env without hardcoding it 
api_key = os.getenv("ABUSEIPDB_API_KEY") # reads .env and loads into a variable every time it runs
                                         # it does this while never hardcoding the API key

for IP in Flagged: #This will loop through every IP address in the list 
     

# we have a list of IP address that are flagged 
# each list has an index number we know that 
# we need to loop through every IP in the list and make an API call on it so we can get info on the IP
# 
        

        
    url = 'https://api.abuseipdb.com/api/v2/check' # this is our endpoint basically where were sending out IP 

    parameters = {  #tells the api what IP were asking for and how many days of data we want
        "ipAddress": IP   , # falgged is a list but the element inside it is a string which want here
        "maxAgeInDays": "30" 
    }

    headers = {
        "Accept": "application/json", # tells the server to send back JSON
        "Key": api_key
    }

    response = requests.request(method='GET', url=url, headers=headers, params=parameters)
    #1. declare a response variable 
    #2. requests.request() which calls the library and the moduel to make a reuqest  
    #3.  we state the method were using for the request 
    #4.  the url we are requesting 
    #5.  the header which is used to authenticate us and tell how we want data to come to us
    #6. params which is used to tell the request what we want back 
        
    decodedResponse = json.loads(response.text) 
    #1. this takes the JSON response and turns it into a a python dictornary so we can 
    #2. we use .text cuz thats what is returned

    # response example 

    #{
        #"data": {
        #"ipAddress": "118.25.6.39",
        #"isPublic": true,
        #"ipVersion": 4,

    # its all nested inside of the data key so you have to call for the data key to query piece of data you wanna show 
    print("----------------------------------------------------------------\n")
    print(f" IP Adreass {IP} \n")
    print(f"AbuseConfidenceScore: {decodedResponse['data']['abuseConfidenceScore']}\n")
    print(f" Internet service provider: {decodedResponse['data']['isp']}\n")
    print(f" Country code: {decodedResponse['data']['countryCode']}\n")
    print(f" Last Reported at: {decodedResponse['data']['lastReportedAt']} \n")
    print("-----------------------------------------------------------------\n")

    





    # we need to take JSON and move it to python reason being we need to be able to dictate the data it needs to be in python 

    # we turn it into a dictionaire so we query the exact data we want 



    # then query this data from the dictoniare 
        # abuseConfidenceScore 
        # countryName 
        # isp 
        # reports

