import discord
from discord.ext import commands
import random
import requests 
import aiohttp
bot_embed_color = 0x4548a8

class Utilities(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['ethereum'])
  async def eth(self, ctx):
      r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
      r = r.json()
      usd = r['USD']
      eur = r['EUR']
      em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
      em.set_author(name='Ethereum', icon_url='https://cdn.disnakeapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
      await ctx.reply(embed=em)


  @commands.command(pass_context=True)
  async def lyrics(ctx, *, song):
       track = song.replace(" ", "+")
       wait = await ctx.reply(f":mag: Please hold on, searching for `{song}`")
       r=requests.get(f'https://some-cool-api.herokuapp.com/lyrics/?lyrics={track}')#This is my API feel free to use it
       try:
           res=r.json()
           title = res['title']
           artist = res['artist']
           lyrics = res['lyrics']
           source = res['source']
           embed = discord.Embed(title=f"**{title}**", description=f"**{artist}**\n\n\n{lyrics}\n", color=bot_embed_color)
           embed.set_footer(text=f"Source: {source}")
           await wait.edit(embed=embed)
       except:
           await wait.edit(content=f"Couldn't find any lyrics for `{song}`. Please try giving a more detailed search.")
      
      
  @commands.command(aliases=['bitcoin'])
  async def eth(self, ctx):
      r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
      r = r.json()
      usd = r['USD']
      eur = r['EUR']
      em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
      em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
      await ctx.reply(embed=em)
    
    
  @commands.command()
  async def pingweb(self, ctx, website = None):
      if website is None: 
          embed=discord.Embed(title="Error!", description="You didn't enter a website to ping for ;-;", color=0x243e7b)
          await ctx.send(embed=embed)
      else:
          try:
              r = requests.get(website).status_code
          except Exception as e:
              await ctx.send(f'''Error raised :- ```{e}```''')
          if r == 404:
              await ctx.send(f'Site is down, responded with a status code of {r}')
          else:
              await ctx.send(f'Site is up, responded with a status code of {r}')

    
  @commands.command(aliases=['pfp', 'avatar'])
  async def av(self, ctx, *, user: discord.Member): 
      av = user.display_avatar.url
      embed = discord.Embed(title="{}'s pfp".format(user.name), description="Here it is!", color=bot_embed_color)
      embed.set_image(url=av)
      await ctx.send(embed=embed)

  
  @commands.command(aliases=['server', 'serverinfo'])
  async def sinfo(self, ctx):
      embed = discord.Embed(title=f"{ctx.guild.name}", description="Here is the server info :-", color=bot_embed_color)
      embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
      embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
      embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
      embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
      embed.set_thumbnail(url=f"{ctx.guild.icon}")
      await ctx.reply(embed=embed)


  @commands.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
  async def geoip(self, ctx, *, ipaddr: str = '1.3.3.7'): 
      r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
      geo = r.json()
      em = discord.Embed()
      fields = [
          {'name': 'IP', 'value': geo['query']},
          {'name': 'ipType', 'value': geo['ipType']},
          {'name': 'Country', 'value': geo['country']},
          {'name': 'City', 'value': geo['city']},
          {'name': 'Continent', 'value': geo['continent']},
          {'name': 'Country', 'value': geo['country']},
          {'name': 'IPName', 'value': geo['ipName']},
          {'name': 'ISP', 'value': geo['isp']},
          {'name': 'Latitute', 'value': geo['lat']},
          {'name': 'Longitude', 'value': geo['lon']},
          {'name': 'Org', 'value': geo['org']},
          {'name': 'Region', 'value': geo['region']},
          {'name': 'Status', 'value': geo['status']},
      ]
      for field in fields:
          if field['value']:
              em.add_field(name=field['name'], value=field['value'], inline=True)
      return await ctx.send(embed=em)

  @commands.command()
  async def truth(self, ctx, rating = None):
    if rating == None:
      r = requests.get(f"https://api.truthordarebot.xyz/api/truth")
      res = r.json()
      Tile = f"Here is a truth for you"
      Desc = res['question']
      embed=discord.Embed(title=Tile, description=Desc, color=bot_embed_color)
      await ctx.reply(embed=embed)
    else:
      try: 
        r = requests.get(f"https://api.truthordarebot.xyz/api/truth/?rating={rating}")
        res = r.json()
        Tile = f"Here is a {rating} rated question for you"
        Desc = res['question']
        embed=discord.Embed(title=Tile, description=Desc, color=bot_embed_color)
        await ctx.reply(embed=embed)
      except:
        await ctx.reply("Please send a valid rating!! Valid parameters are `pg`,`pg13`,`r`")

  @commands.command()
  async def dare(self, ctx, rating = None):
    if rating == None:
      r = requests.get(f"https://api.truthordarebot.xyz/api/dare")
      res = r.json()
      Tile = f"Here is a dare for you"
      Desc = res['question']
      embed=discord.Embed(title=Tile, description=Desc, color=bot_embed_color)
      await ctx.reply(embed=embed)
    else:
      try: 
        r = requests.get(f"https://api.truthordarebot.xyz/api/dare/?rating={rating}")
        res = r.json()
        Tile = f"Here is a {rating} rated question for you"
        Desc = res['question']
        embed=discord.Embed(title=Tile, description=Desc, color=bot_embed_color)
        await ctx.reply(embed=embed)
      except:
        await ctx.reply("Please send a valid rating!! Valid parameters are `pg`,`pg13`,`r`")
  
def setup(bot):
  bot.add_cog(Utilities(bot))
