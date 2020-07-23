import discord
from discord.ext import commands

TOKEN = 'NzM1MzA4NDQ5NjYyODk0MTYw.XxeXsw.it4mV6jAkvAl3gFsT2_T1zLH5Fs'
client = commands.Bot(command_prefix='.')

#  EVENTS


@client.event
async def on_ready():
    print('PartyHole Bot Booting...\nInitializing...\nBooted successfully.')


#  COMMANDS


@client.command(brief='Returns pong!', description='Calculates client to server to bot in ms.')
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(brief='Command for Walrus.', description='Command for our favorite walrus.')
async def walrus(ctx):
    await ctx.send('<@234827351458840577> is the sexiest man alive :heart_eyes:')


@client.command(brief='Command for Brockstar.', description='Command for boob :heart_eyes:.')
async def brock(ctx):
    await ctx.send('<@325080492451823616> is on the futon and will give you that penis')


@client.command(brief='Command for Justin.', description='He\'s a dad, literally.')
async def justin(ctx):
    await ctx.send('<@404109013740027906> is a broke bitch... Spare him some change')


@client.command(brief='Command for Brandon.', description='No one has ever seen him and Batman in the same room...')
async def party(ctx):
    await ctx.send('<@298583116229115905> https://i.kym-cdn.com/photos/images/original/000/941/408/7aa.jpg')


@client.command(brief='Command for Hyde.', description='You really expect me to write a help page for my own command?')
async def hyde(ctx):
    await ctx.send('<@90650772458471424> :a:')


@client.command(brief='Command for Heath.', description='He doesn\'t really have a negative IQ.', aliases=['bigferg'])
async def heath(ctx):
    await ctx.send('Negative IQ')


@client.command(brief='Use .zip', description='Remember to hydrate kids.', aliases=['zip'])
async def zip_foo(ctx):
    await ctx.send('ferzst let mi taek a zippa wadda')


@client.command(brief='Clears messages', description='Clears messages, do .clear number_of_message_to_clear')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run(TOKEN)
