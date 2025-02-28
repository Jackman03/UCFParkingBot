#!/usr/bin/env python3
#Program to dump JSON data from the Parking Services API
#11/25/2024
#Jackson Vaughn

import requests
import json
from datetime import datetime

#Constant
#Hopefully this url wont change...
URL = 'https://secure.parking.ucf.edu/GarageCounter/GetOccupancy'


#Prints out the needed garage info to the console for debugging   
def DebugGarages(ParkingData,PreviousData):
     for Garage in range(0,9):
    #For each garage print out the name, available and total spots.
    #We know there are 9 garages/lots
        GarageName = ParkingData[Garage]['location']['name']
        GarageAvailable = int(ParkingData[Garage]['location']['counts']['available'])
        GarageTotal = int(ParkingData[Garage]['location']['counts']['total'])
        GarageOccupied = int(ParkingData[Garage]['location']['counts']['occupied'])
        GarageChange = int(ParkingData[Garage]['location']['counts']['available']) - int(PreviousData[Garage]["GarageAvailibility"])


        #Prints out for debugging
        print(f'Garage: {GarageName}')
        print(f'Spots available: {GarageAvailable}')
        print(f'Total spots: {GarageTotal}')
        print(f'Occupied spots: {GarageOccupied}')
        print(f'Amount changed: {GarageChange}')
        curtime = datetime.now().strftime('%Y-%m-%d%H:%M:%S.%f')
        print(f'{curtime}\n')
        

#dumps the JSON into a file for keeping.
def DumpJSON(URL: str,debug:bool):
    #send GET request
    
    r = requests.get(URL)

    code = r.status_code

    if code != 200:
         print(code)
         print(f'https://http.cat/{code}')
         return
   
    
    #Loads request json into an object
    ParkingData = r.json()
    
    
    #dump JSON into a file for easier viewing
    with open('src/data/ParkingData.json' , 'w') as json_file:
        json.dump(ParkingData, json_file,indent=4)
    print('Dump Successful')

    #Load the previous data so we can calculate the availibity change
    #Current spaces - previous spaces
    
    with open('src/data/Garages.json' , 'r') as json_file:
        PreviousData = json.load(json_file)
  
    
    if debug: DebugGarages(ParkingData,PreviousData)
    #Filter the orginal data to only get what name, avilibility, total spots, and occupied spots
    #These will be passed to the js file to be put on the web
    BetterParkingData = [{"GarageName": ParkingData[Garage]['location']['name'], 
                          "GarageAvailibility": int(ParkingData[Garage]['location']['counts']['available']),
                          "TotalSpots": int(ParkingData[Garage]['location']['counts']['total']),
                          "TotalOccupied": int(ParkingData[Garage]['location']['counts']['occupied']),
                          "Timestamp": datetime.now().strftime('%Y-%m-%d%H:%M:%S.%f'),
                          "AmountChanged": int(ParkingData[Garage]['location']['counts']['available']) - int(PreviousData[Garage]["GarageAvailibility"])
                        }for Garage in range(0,9)]
    
    
    #Dumps filtered JSON to be read by a js file
    #Also used to find the avilibility change
    try:
        with open('src/data/Garages.json' , 'w') as json_file:
                json.dump(BetterParkingData, json_file,indent=4)
    except Exception as e: 
        print(e)
        print('JSON failed to save')
        

    
    #
    


    
DumpJSON(URL,True)
