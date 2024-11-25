import requests
import json

url = 'https://secure.parking.ucf.edu/GarageCounter/GetOccupancy'





#dumps the JSON into a file for keeping.
def DumpJSON(url):
    #send GET request

    try:
        r = requests.get(url)
    except:
        print(Exception)

    #dump JSON into a file for easier viewing
    ParkingData = r.json()
    with open('ParkingData.json' , 'w') as json_file:
        json.dump(ParkingData, json_file,indent=4)

    #For each garage print out the name, available and total spots.
    GarageName = ParkingData[0]['location']['name']
    GarageAvailable = ParkingData[0]['location']['counts']['available']
    GarageTotal = ParkingData[0]['location']['counts']['total']
    print(f'Garage: {GarageName}')
    print(f'Spots available: {GarageAvailable}')
    print(f'Total spots: {GarageTotal}')

DumpJSON(url)
