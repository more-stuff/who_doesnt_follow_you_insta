import discord #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
import datetime
import instaloader
from time import sleep

L = instaloader.Instaloader()
# Login with the bot
user = ''
password = ''


L.login(user, password)


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
    print(follower_list)
    print(followed_list)
    return follower_list, followed_list



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
    follower_list, followed_list = check_unfollowed(username)
    for followed in followed_list:
        if follower_list.count(followed) == 0:
            non_follower_str+= f'{followed}\n'
            non_follower_str += f"https://www.instagram.com/{followed}\n"
            await ctx.send(non_follower_str)
            non_follower_str = ''





@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_help"))
    print('My bot is ready')


bot.run('')

