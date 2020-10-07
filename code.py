import time
import discord
from discord.ext import commands
from random import randint,choice
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure
import config
import asyncio
import os
import youtube_dl
import shutil
vol = 0.5
bot = commands.Bot(command_prefix='/')
bot.remove_command('help')
@bot.event
async def on_ready():
     print('Бот подключён')
     await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Waiting a command"))
@bot.command(pass_context=True)
@has_permissions(kick_members=True)
async def kick( ctx, member: discord.Member, *, reason = ''):
    Adminchat = get(ctx.guild.channels, name='notices')
    author = ctx.message.author
    try:    
        await ctx.channel.purge( limit = 1 )
        await member.kick( reason = reason )
        embed=discord.Embed(title='Kick', description='Moderator has been kick member', color=0x300080)
        embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
        embed.add_field(name='Moderator' , value=f'{ author.mention }', inline=False)
        embed.add_field(name='reason' , value=f'{ reason }', inline=False)
        embed.set_footer(text='Author of bot jwix777')
        await Adminchat.send(embed=embed)
        pass
    except PermissionError :
        await ctx.send('You dont have permissions :(') 
        pass
@bot.command(pass_context=True)
@has_permissions(ban_members=True)
async def ban( ctx, member: discord.Member, *,reason = ''):   
    await ctx.channel.purge( limit = 1 )
    await member.ban( reason = reason )
    user = member
    await ctx.send(f'Banned user { user.mention } for { reason }')
@bot.command(pass_context=True)
@has_permissions(ban_members=True)
async def unban( ctx,* ,member ):
    await ctx.channel.purge( limit = 1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban( user )
        await ctx.send(f'Unbanned user { user.mention }')
    pass 
@bot.command(pass_context=True)
@has_permissions(manage_roles=True)
async def mute( ctx, member: discord.Member=None,t: int=None,h: str=None,*, reason: str=None):   
    author = ctx.message.author
    if h=="s":
        f = t
        mute_role = get(ctx.guild.roles, name= 'Muted')
        await member.add_roles(mute_role)
        embed=discord.Embed(title='Mute', description='Moderator muted member', color=0x500080)
        embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
        embed.add_field(name='Moderator' , value=f'{ author.mention }', inline=False)
        embed.add_field(name='reason' , value=f'{ reason }', inline=False)
        embed.add_field(name='Time' , value=f'{ t } seconds', inline=False)
        embed.set_footer(text='Author of bot jwix777')
        await ctx.send(embed=embed)
        await asyncio.sleep(f)
        await member.remove_roles(mute_role)
        embed=discord.Embed(title='Unmute', description='Autounmute', color=0x500080)
        embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
        embed.add_field(name='Moderator' , value='Botadmin777', inline=False)
        embed.add_field(name='reason' , value=f'Mute expired', inline=False)
        embed.set_footer(text='Author of bot jwix777')
        await ctx.send(embed=embed)
        pass
    if h=="m":
        f = t*60
        mute_role = get(ctx.guild.roles, name= 'Muted')
        await member.add_roles(mute_role)
        embed=discord.Embed(title='Mute', description='Moderator muted member', color=0x500080)
        embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
        embed.add_field(name='Moderator' , value=f'{ author.mention }', inline=False)
        embed.add_field(name='reason' , value=f'{ reason }', inline=False)
        embed.add_field(name='Time' , value=f'{ t } minutes', inline=False)
        embed.set_footer(text='Author of bot jwix777')
        await ctx.send(embed=embed)
        await asyncio.sleep(f)
        await member.remove_roles(mute_role)
        embed=discord.Embed(title='Unmute', description='Autounmute', color=0x500080)
        embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
        embed.add_field(name='Moderator' , value='Botadmin777', inline=False)
        embed.add_field(name='reason' , value=f'Mute expired', inline=False)
        embed.set_footer(text='Author of bot jwix777')
        await ctx.send(embed=embed)
    if h=="h":
        f = t*3600
        mute_role = get(ctx.guild.roles, name= 'Muted')
        await member.add_roles(mute_role)
        embed=discord.Embed(title='Mute', description='Moderator muted member', color=0x500080)
        embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
        embed.add_field(name='Moderator' , value=f'{ author.mention }', inline=False)
        embed.add_field(name='reason' , value=f'{ reason }', inline=False)
        embed.add_field(name='Time' , value=f'{ t } hours', inline=False)
        embed.set_footer(text='Author of bot jwix777')
        await ctx.send(embed=embed)
        await asyncio.sleep(f)
        await member.remove_roles(mute_role)
        embed=discord.Embed(title='Unmute', description='Autounmute', color=0x500080)
        embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
        embed.add_field(name='Moderator' , value='Botadmin777', inline=False)
        embed.add_field(name='reason' , value=f'Mute expired', inline=False)
        embed.set_footer(text='Author of bot jwix777')
        await ctx.send(embed=embed)
    if h=="d":
        f = t*86400
        mute_role = get(ctx.guild.roles, name= 'Muted')
        await member.add_roles(mute_role)
        embed=discord.Embed(title='Mute', description='Moderator muted member', color=0x500080)
        embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
        embed.add_field(name='Moderator' , value=f'{ author.mention }', inline=False)
        embed.add_field(name='reason' , value=f'{ reason }', inline=False)
        embed.add_field(name='Time' , value=f'{ t } days', inline=False)
        embed.set_footer(text='Author of bot jwix777')
        await ctx.send(embed=embed)
        await asyncio.sleep(f)
        await member.remove_roles(mute_role)
        embed=discord.Embed(title='Unmute', description='Autounmute', color=0x500080)
        embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
        embed.add_field(name='Moderator' , value='Botadmin777', inline=False)
        embed.add_field(name='reason' , value=f'Mute expired', inline=False)
        embed.set_footer(text='Author of bot jwix777')
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Error", description="Too few arguments", color=0xe41111)
        embed.add_field(name="Syntax", value="/mute member time type of time(s. m. h d)  reason", inline=True)
        embed.add_field(name="example", value="/mute @jwix777#0000 5 m very smart :)", inline=False)
        await ctx.send(embed=embed)
@bot.command(pass_context=True)
@has_permissions(manage_roles=True)
async def unmute( ctx, member: discord.Member, *, reason = ''):
    await ctx.channel.purge( limit = 1 )
    mute_role = get(ctx.guild.roles, name= 'Muted')
    await member.remove_roles(mute_role)
    await ctx.send(f" { member } has been unmuted")
@bot.command(pass_context=True)
async def report(ctx, member: discord.Member,*, reason = ''):
    Admin = get(ctx.guild.roles, name='Admin')
    Adminchat = get(ctx.guild.channels, name='notices')
    author = ctx.message.author
    embed=discord.Embed(title='Report', description='Member has been sent report', color=0x400080)
    embed.add_field(name='Member', value=f'{ member.mention }', inline=False)
    embed.add_field(name='Reported' , value=f'{ author.mention }', inline=False)
    embed.add_field(name='Report reason' , value=f'{ reason }', inline=False)
    embed.set_footer(text='Author jwix777')
    await Adminchat.send(embed=embed)
    await Adminchat.send(f'{ Admin.mention }')
    await ctx.send(f'{ author.mention } report sent')
@bot.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    author = ctx.message.author
    embed=discord.Embed(title= 'Hug', color=0x300080)
    embed.add_field(name=':)', value =f'{ author.mention } hug { member.mention }')
    embed.set_image(url='https://media1.tenor.com/images/3820ad0d9611dfc9c492e3d689b11c23/tenor.gif?itemid=15793127')
    await ctx.send(embed=embed)
    pass
@bot.command(pass_context=True)
async def five(ctx, member: discord.Member):
    author = ctx.message.author
    embed=discord.Embed(title= 'Five', color=0x300080)
    embed.add_field(name=':)', value =f'{ author.mention } gave five { member.mention }')
    embed.set_image(url='https://media1.tenor.com/images/7b1f06eac73c36721912edcaacddf666/tenor.gif?itemid=10559431')
    await ctx.send(embed=embed)
    pass
@bot.command(pass_context=True,)
async def help(ctx):
    embed=discord.Embed(title="Help", description="Commands commands and commands", color=0x00e4f5)
    embed.set_author(name="jwix777")
    embed.add_field(name="ban ", value="ban member. Need permission ban_members", inline=False)
    embed.add_field(name="five  ", value="Just Rp command for fun :)", inline=False)
    embed.add_field(name="help", value="Shows this message", inline=False)
    embed.add_field(name="hug", value="Just Rp command for fun :)", inline=False)
    embed.add_field(name="mute", value="mute member. Need permission manage_roles", inline=False)
    embed.add_field(name="kick", value="kick members. Need permission kick_members", inline=False)
    embed.add_field(name="report", value="send report for a violator. For members.", inline=False)
    embed.add_field(name="unban", value="unban member. Need permission ban_members", inline=False)
    embed.add_field(name="unmute", value="unmute member. Need permission manage_roles", inline=False)
    embed.set_footer(text="Support server https://discord.gg/SEk4DsW")
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def command(ctx, command):
    if command=='ban':
        embed=discord.Embed(title="Help", description="Command ban", color=0xf3f702)
        embed.add_field(name="Syntax ", value="ban member reason", inline=False)
        embed.add_field(name="description", value="ban member", inline=False)
        embed.add_field(name="need permission", value="ban_members", inline=False)
        embed.set_footer(text="support server https://discord.gg/SEk4DsW")
        await ctx.send(embed=embed)
        ok
        pass
    if command=='five':
        embed=discord.Embed(title="Help", description="Command five", color=0xf3f702)
        embed.add_field(name="Syntax ", value="five member", inline=False)
        embed.add_field(name="description", value="give five to member. RP command for fun", inline=False)
        embed.set_footer(text="support server https://discord.gg/SEk4DsW")
        await ctx.send(embed=embed)
        ok
        pass
    if command=='kick':
        embed=discord.Embed(title="Help", description="Command kick", color=0xf3f702)
        embed.add_field(name="Syntax ", value="kick member reason", inline=False)
        embed.add_field(name="description", value="kick member", inline=False)
        embed.add_field(name="need permission", value="kick_members", inline=False)
        embed.set_footer(text="support server https://discord.gg/SEk4DsW")
        await ctx.send(embed=embed)
        ok
        pass
    if command=='hug':
        embed=discord.Embed(title="Help", description="Command hug", color=0xf3f702)
        embed.add_field(name="Syntax ", value="hug member", inline=False)
        embed.add_field(name="description", value="hug member. RP command for fun", inline=False)
        embed.set_footer(text="support server https://discord.gg/SEk4DsW")
        await ctx.send(embed=embed)
        ok
        pass
    if command=='mute':
        embed=discord.Embed(title="Help", description="Command mute", color=0xf3f702)
        embed.add_field(name="Syntax ", value="mute member time(1-30) type of time(s m h d) reason", inline=False)
        embed.add_field(name="description", value="mute member", inline=False)
        embed.add_field(name="types of time", value="s - second, m - minute, h - hours, d - day, ", inline=False)
        embed.add_field(name="need permission", value="manage_roles", inline=False)
        embed.set_footer(text="support server https://discord.gg/SEk4DsW")
        await ctx.send(embed=embed)
        ok
        pass
    if command=='report':
        embed=discord.Embed(title="Help", description="Command report", color=0xf3f702)
        embed.add_field(name="Syntax ", value="report member reason", inline=False)
        embed.add_field(name="description", value="report member. And justice will be served ", inline=False)
        embed.set_footer(text="support server https://discord.gg/SEk4DsW")
        await ctx.send(embed=embed)
        ok
        pass
    if command=='unmute':
        embed=discord.Embed(title="Help", description="Command unmute", color=0xf3f702)
        embed.add_field(name="Syntax ", value="unmute member reason", inline=False)
        embed.add_field(name="description", value="unmute member", inline=False)
        embed.add_field(name="need permission", value="manage_roles", inline=False)
        embed.set_footer(text="support server https://discord.gg/SEk4DsW")
        await ctx.send(embed=embed)
        ok
        pass
    if command=='unban':
        embed=discord.Embed(title="Help", description="Command unban", color=0xf3f702)
        embed.add_field(name="Syntax ", value="unban member reason", inline=False)
        embed.add_field(name="description", value="unban member", inline=False)
        embed.add_field(name="need permission", value="ban_members", inline=False)
        embed.set_footer(text="support server https://discord.gg/SEk4DsW")
        await ctx.send(embed=embed)
        ok
        pass
token = os.environ.get('BOT_TOKEN')
bot.run(token)
