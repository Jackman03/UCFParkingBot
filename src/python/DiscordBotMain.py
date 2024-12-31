#!/usr/bin/env python3
#Jackson vaughn
#Driver for the main discord bot
import json
import discord
from datetime import datetime, date
import time
from discord.ext import tasks, commands
import os
from dotenv import load_dotenv
import requests
import asyncio
from GetGarageJSON import DumpJSON, URL


def Configure():
    load_dotenv()
    DumpJSON(URL,False) #refresh data on startup

#the start of a command prefix. when a user types a $ the bot will be registered
intents = discord.Intents.all()
intents.message_content = True
intents.members = True

CHANNEL_ID = os.getenv('ChannelID')

bot = commands.Bot(command_prefix = '!',intents=intents)

@bot.event
#sets up first command
async def on_ready():
    print("Bot is loaded")
    await bot.wait_until_ready()
   


#Commands
#Garage (x) returns information about a specific garage
#map returns the JS map of the parking counts

@bot.command()
async def ListAll(ctx):

    with open('src/data/Garages.json' , 'r') as json_file:
        Data = json.load(json_file)

    for Garage in Data:

        await ctx.send(f'`Garage: {Garage['GarageName']}\n'+ 
        f'Spots available: {Garage['GarageAvailibility']}\n'+
        f'Occupied spots: {Garage['TotalOccupied']}\n'+
        f'Amount changed: {Garage['AmountChanged']}`\n\n')


@bot.command()
async def ListGarages(ctx):

    with open('src/data/Garages.json' , 'r') as json_file:
        Data = json.load(json_file)

    for Garage in Data:
        await ctx.send(f'`Garage: {Garage['GarageName']}`\n\n')

#Command to get Garage
@bot.command()
async def Garage(ctx,*,garage:str):

    await ctx.send(garage)
    with open('src/data/Garages.json' , 'r') as json_file:
        Data = json.load(json_file)

    for Garage in Data:

        if Garage['GarageName'] == garage:
            await ctx.send(f'`Garage: {Garage['GarageName']}\n'+ 
            f'Spots available: {Garage['GarageAvailibility']}\n'+
            f'Occupied spots: {Garage['TotalOccupied']}\n'+
            f'Amount changed: {Garage['AmountChanged']}`\n\n')
            return

    await ctx.send('Garage not found')

#Help Command
@bot.command()
async def Help(ctx):
    await ctx.send('`UCF Parking Bot help menu\n' +
                   'ListAll - Lists all of the current Garages and there numbers\n'+
                   'Garage (Garage Name) - Lists the current numbers for the specified garage\n'+
                   'ListGarages - Lists all of the availible garages\n'+
                   'Help - Displays the help menu`')

#Displays the parking map from the website 
@bot.command()
async def Map(ctx):
    url = 'http://127.0.0.1:5500/src/html/' #funny default URL
    #url = "https://en.wikipedia.org/wiki/Special:Random"
    try:
        r = requests.get(url)
    except:
        print('Request Failed')
        print(Exception)
    #uses the requests libary to send a http get to the url, then sends back a random article
    WebPage = discord.Embed()
    WebPage = discord.Embed(title="UCF Parking Helper", url=url, description="Map of UCF Parking")

    await ctx.send(embed=WebPage)

@bot.command()
async def SendParkingUpdate(ctx):
    channel = bot.get_channel(1321193900752506921)
    await channel.send('Hello world')
 


@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("Sorry, I don't recognize that command. Type `!Help` for a list of available commands.")
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(f"Missing arguments for the command. Please provide all necessary parameters.")
    else:
        await ctx.send(f"An error occured: {str(error)}")


@bot.event
async def on_disconnect():
    print('Disconnected')
    
                   
Configure()
bot.run(os.getenv('DiscordKey'))



