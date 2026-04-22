

# find failed logins 

# open / add  the file
# create a for loop to loops through each line 
# We wanna display only the IP, USER, TIME, Failed Password
# when we take a filed line its a String 
# we need to be able to parse it so we can pull bits and piece of data we want 
# we could use split since it takes a string and breaks up all the words into a list and since all the logs have the same assests itll work

#PLAN
   # we need an If condintions so if there is "failed"
        # 
        # once foudn we are gonna split it into a list 
        # then your gonna print index 10
        # do the same for USER = 8 and TIME = 2
        # data is just the first index so it would be like [0,1]
        # print them 

from collections import Counter

with open("IP project\sample_auth.log") as file:
    
    IP_Failed = []

    Total_Fail = 0 
    print("\n")
    print("ERRORS FOUND")
    print("----------------------------------------------------------------") 
    for line in file:
        
        if "Failed" in line: # finds lins that are failed
            Total_Fail += 1
            
            Found_line = line.split() # takes the line and split i

            Find_IP = Found_line.index("from") # gets the index location the word before the ip 

            IP_Failed.append(Found_line[1 + Find_IP]) # adds this too IP_failed list 

            print (f"IP Address {Found_line[1 + Find_IP]}   User: {Found_line[8]}  Date and Time: {Found_line[0:3]}\n")#prints all wanted info
             


IP_failed_list = Counter(IP_Failed) # counts the list frequency of each IP and gives back a dict like this [IP(key):count(value)]

# example Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})


Flagged = [] # this will store the Flagged IP Adresses 



for IP , count in IP_failed_list.items():

# loop works like this IP(key) and count(value) place holders for key:value in our dict
# we use .item(); to split key and value into item but there are still in the same list spot 
# example output dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
    
    if count >= 3: #checks the value of the item and sees if its greater than of equal to 3
        print("----------------------------------------------------------------\n") 
        print(f"Flagged IP {IP}\n") # prints whatever that values IP which is this key placeholder
        print("----------------------------------------------------------------\n") 
        Flagged.append(IP) # stores the flagged IP in the Flagged List 



    

print (f"Total fails {Total_Fail}\n")   
print("----------------------------------------------------------------")      

# Ip reputation Checker 

# what are we doing 
# using the flagged Ip we are going to create an API call to AbuseIPDB and itll give back info if its been reported for abuse

#get endpoint for AbuseIPDB 
#endpoint => https://www.abuseipdb.com/check/[IP]/json?key=[API_KEY]&days=[DAYS]



# 1. create a api call using the endpoint were gonna use the GET method 

# import request library which has methods to create an API call to the endpoint

# import json library abuse gives back JSON so we need to convert that into python so we can use it 

# we would have to declare the [IP] and [API_KEY] variables so it would then go into the URl variable

# how would we get declare the [IP] ?
# we would just put what we flagged we found into a varible 

# how are we gonna implment an API Key ?
# make a seperate file .env 
# this will store my file under a variable 
# but we must then import that variable into this file 
# so then we can put that into the API_KEY placeholder for the api call


# make a URL variable would be the the endpoint 

# we would implment the falgged ip and api key and days (harddcoded day)




# how will it respond like what would be the output 


# how are we gonna implement an API key ?
# make a seperate file .env 
# this will store my file under a variable 
# but we must then import that variable into this file 
# so then we can put that into the API_KEY placeholder for the api call


# How are we gonna implement days ? 
# we could hard code it as like 7 days 





       
        
     



        
        
        
        
        
        
        
     





