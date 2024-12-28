#Automaticly refreshes the parking json every 10 minuets
import GetGarageJSON as JSONControl
import time

#This will send the data to the webhook as well
def AutoRefresh(TimeSpace: int):

    while True:
        JSONControl.DumpJSON(JSONControl.URL,True)
        time.sleep(TimeSpace)



AutoRefresh(120)