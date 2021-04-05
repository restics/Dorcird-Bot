import discord.ext.commands as cmd
import imageedit as ie
import discord as dc


token = 'ODI4MDU0MjA5OTk5NjY3MjAw.YGj_lA.wEW5eQsjgUJgkAK381ZLmqKGBkE'
client = cmd.Bot(command_prefix='cum ')


@client.event
async def on_ready():
    print('bot is ready')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel
    args = message.content.split(" ")
    args.pop(0) #command keyword

    if message.content.startswith('test'):
      await channel.send("Test Message")


    elif message.content.startswith('soychad'):
        first_message = second_message = "either you didnt specify anyone, or this person hasnt said shit recently"

        # if you dont put args stuff can change
        if len(args) != 0:
          async for msg in channel.history(limit=20):
              if msg.author == message.author and not msg.content.startswith('soychad'):
                  first_message = msg.content
                  break
          
          
          async for msg in channel.history(limit=20):
              if str(msg.author.id) == str(args[0][3:-1]):
                  second_message = msg.content
                  break
        
        

        ie.create_meme(second_message, first_message)
        await channel.send("", file=dc.File('copy.png'))


client.run(token)
