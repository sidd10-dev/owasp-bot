import discord
import firebase_admin
from firebase_admin import credentials,db
from discord.ext import commands
client = commands.Bot(command_prefix = '!')
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://owasp-test-855b8-default-rtdb.firebaseio.com/'
})

ref = db.reference('Certificates')
add = db.reference('Data')


counter = 0

@client.event
async def on_ready():
    print("STFU and go to discord!")

@client.command()
async def addCertificate(ctx, member: discord.Member, *,namedeptyear):
    List = namedeptyear.split(',')
    name = List[0]
    dept = List[1]
    year = List[2]
    maincounter=0
    damn = add.get()
    for i in damn.values():
        if i['Id']==member.discriminator and i['Name']==name :
            ref.child(f'{member.name}').push({
                'Discord_Id':member.discriminator,
                'Name':name,
                'Department':dept,
                'Year':year,
            })
            await ctx.send('User id,name verified ........Certificate added !')
            maincounter=1
            break
        
    if maincounter==0:
        await ctx.send(f'smthng is fishhhhyyyy...{ctx.message.author.name} is recommended to wear specs')

    

@client.command()
async def adddata(ctx,member:discord.Member,*,name):
   add.push({
       'Id':member.discriminator,
       'Name': name
   })
   await ctx.send('Data added . Reference "data" for certification')
   
@client.command()
async def bye(ctx):
    await client.close()


client.run('ODQ0ODYzMDE0MTE2MjYxOTAx.YKYl_w.nXxyhcvRv3OwZuw1aPVZ3bdjTo0')
