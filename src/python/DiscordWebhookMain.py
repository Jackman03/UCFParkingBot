#!/usr/bin/env python3
#Automaticly refreshes the parking json every 10 minuets
import GetGarageJSON as JSONControl
import time
from datetime import datetime, timedelta
from dhooks_lite import Webhook

import json
import os
from dotenv import load_dotenv



def RunHook():
    DISCORD_WEBHOOK_URL = os.getenv('Hook')
    hook = Webhook(DISCORD_WEBHOOK_URL)

    with open('src/data/Garages.json' , 'r') as json_file:
        Data = json.load(json_file)

    curtime = datetime.now().strftime('%H:%M:%S')
    hook.execute(f'UCF Parking numbers as of {curtime}')
    for Garage in Data:

        hook.execute(f'`Garage: {Garage['GarageName']}\n'+ 
            f'Spots available: {Garage['GarageAvailibility']}\n'+
            f'Occupied spots: {Garage['TotalOccupied']}\n'+
            f'Amount changed: {Garage['AmountChanged']}`\n\n')
    PrevTime = datetime.now() - timedelta(minutes=15)
    hook.execute(f'Last updated: {PrevTime}')

#This will send the data to the webhook as well
def AutoRefresh(TimeSpace: int):
        
        load_dotenv()

        while True:
            try:
                JSONControl.DumpJSON(JSONControl.URL,True)
                curtime = datetime.now().strftime('%Y-%m-%d%H:%M:%S.%f')
                print(f'JSON dump succeded {curtime}')
                RunHook()
                time.sleep(TimeSpace) #sleep for 3 minuets

            except Exception as e: print(e)
        
AutoRefresh(900)