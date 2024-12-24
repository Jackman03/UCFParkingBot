#Jackson vaughn
#Driver for the main discord bot
import json
import discord
import datetime as datetime
from discord.ext import commands
import os
from dotenv import load_dotenv


def Configure():
    load_dotenv()


ChanelID = os.getenv('DiscordKey')
#the start of a command prefix. when a user types a $ the bot will be registered
intents = discord.Intents.all()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = '$',intents=intents)

@client.event
#sets up first command
async def on_ready():
    print("Bot is loaded")


#Commands
#Garage (x) returns information about a specific garage
#map returns the JS map of the parking counts

@client.command()
async def DisplayParking():

    with open('src/data/Garages.json' , 'r') as json_file:
        Data = json.load(json_file)

    for Garage in Data:


        print(f'Garage: {Garage['GarageName']}')
        print(f'Spots available: {Garage['GarageAvailibility']}')
        print(f'Occupied spots: {Garage['TotalOccupied']}')
        print(f'Amount changed: {Garage['AmountChanged']}')
        print('\n')

DisplayParking()
