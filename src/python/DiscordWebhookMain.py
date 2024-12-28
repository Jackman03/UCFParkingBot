#Automaticly refreshes the parking json every 10 minuets
import GetGarageJSON as JSONControl
import time
from datetime import datetime

from dhooks import webhook

#This will send the data to the webhook as well
def AutoRefresh(TimeSpace: int):

    
        try:
            JSONControl.DumpJSON(JSONControl.URL,True)
            curtime = datetime.now().strftime('%Y-%m-%d%H:%M:%S.%f')
            print(f'JSON dump succeded {curtime}')
            curhour = datetime.now().strftime('%M')
            print(curhour)
            if curhour == '47': print('good time')

        except:
            print(Exception)
        
        


AutoRefresh(1)