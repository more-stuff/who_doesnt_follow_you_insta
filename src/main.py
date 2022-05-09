import discord #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
import datetime
import instaloader
from time import sleep

L = instaloader.Instaloader()
# Login with the bot
L.login('who_doesnt_follow_you', '456rty123qwe')


def check_unfollowed(username):
    # Obtain profile metadata
    profile = instaloader.Profile.from_username(L.context, username)
    follower_list = []
    count_follower = 0
    for followee in profile.get_followers():
        follower_list.append(followee.username)
        count_follower = count_follower + 1

    followed_list = []
    count_followed = 0
    for followee in profile.get_followees():
        followed_list.append(followee.username)
        count_followed = count_followed + 1

    non_follower_list = []

    for followed in followed_list:
        if follower_list.count(followed) == 0:
            non_follower_list.append(followed)

    return non_follower_list



bot = commands.Bot(command_prefix='@', description="this is a testing bot")


#Ping-pong
@bot.command()
async def ping(ctx):
     await ctx.send('pong')

@bot.command()
async def say(ctx, arg1, arg2):
     await ctx.send(arg2)


@bot.command()
async def insta(ctx, username):
    await ctx.send('Loading...')
    non_follower_str = ''
    for user in check_unfollowed(username):
        non_follower_str+= f'{user}\n'
        non_follower_str += f"https://www.instagram.com/{user}\n"
        await ctx.send(non_follower_str)
        non_follower_str = ''





@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_help"))
    print('My bot is ready')


bot.run('OTcyOTAzODgzMzcyMzg4Mzgz.Grc4CO.7jn_IUOX5gkjwYA6GFixnpdX97sDQx29T3BH2o')