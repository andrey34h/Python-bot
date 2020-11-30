import discord
from discord.ext import commands
import asyncio

#Prefix
bot = commands.Bot(command_prefix = "%")

#remove commands
bot.remove_command("help")

#Comandos
@bot.command()
async def sumar(ctx, one:int, two:int):
    await ctx.send(one+two)

@bot.command()
async def test(ctx):
    await ctx.send("Tested")

@bot.command()
async def restar(ctx, one:int, two:int):
    embed = discord.Embed(color=discord.Colour.blue())
    embed.add_field(name="Valor", value=f"valor: {one - two}")
    await ctx.send(embed=embed)


#embeds
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help | Bot testing", color=discord.Colour.blue())
    embed.add_field(name="Help1", value="Esta es una prueba!")
    embed.set_image(url="https://www.python.org/static/img/python-logo.png")
    await ctx.send(embed=embed)

#Eventos
@bot.event 
async def on_ready():
    print("Bot activate")

#Run bot
bot.run("NzgyMzY5ODI4NjIyODI3NTIw.X8LMrg.UghFwmTdHEaIng2QyhAj0N2NNk8")