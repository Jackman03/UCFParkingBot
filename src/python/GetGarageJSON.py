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
        GarageChange = int(ParkingData[Garage]['location']['counts']['available']) - int(PreviousData[Garage]["Garage Availibility"])


        #Prints out for debugging
        print(f'Garage: {GarageName}')
        print(f'Spots available: {GarageAvailable}')
        print(f'Total spots: {GarageTotal}')
        print(f'Occupied spots: {GarageOccupied}')
        print(f'Amount changed: {GarageChange}')
        

#dumps the JSON into a file for keeping.
def DumpJSON(URL):
    #send GET request
    try:
        r = requests.get(URL)
    except:
        print(Exception)
    
    
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

    #Filter the orginal data to only get what name, avilibility, total spots, and occupied spots
    #These will be passed to the js file to be put on the web
    BetterParkingData = [{"Garage Name": ParkingData[Garage]['location']['name'], 
                          "Garage Availibility": int(ParkingData[Garage]['location']['counts']['available']),
                          "Total Spots": int(ParkingData[Garage]['location']['counts']['total']),
                          "Total Occupied": int(ParkingData[Garage]['location']['counts']['occupied']),
                          "Timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
                          "Amount Changed": int(ParkingData[Garage]['location']['counts']['available']) - int(PreviousData[Garage]["Garage Availibility"])
                        }for Garage in range(0,9)]
    
    #Dumps filtered JSON to be read by a js file
    #Also used to find the avilibility change
    with open('src/data/Garages.json' , 'w') as json_file:
            json.dump(BetterParkingData, json_file,indent=4)


    #
    


    
DumpJSON(URL)
