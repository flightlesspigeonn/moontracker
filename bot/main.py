import discord
from discord.ext import commands
import os
from utils.checks import check
from utils.lunation import calculate

intents = discord.Intents.all()
check = check()
bot = commands.Bot(command_prefix='!',intents=intents)
perms = discord.Permissions(permissions=274878032896)

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def phase(ctx):
  """ Sends the current moon phase """
  await ctx.send(calculate())


@bot.command(hidden=True)
@check.is_owner()
async def down(ctx):
  await ctx.send('Shutting Down...')
  print('{0.user} is shutting down...'.format(bot))
  await bot.close()

  
@bot.command()
async def invite(ctx):
  url = discord.utils.oauth_url(client_id=check.grab_id(), permissions=perms)
  file = discord.File("moon.png", filename = "moon.png")
  embed = discord.Embed(title="Invite Me!", url=url, description="Follow this link to invite me to your server.")
  embed.set_thumbnail(url='attachment://moon.png')
  await ctx.send(file=file, embed=embed)


if __name__ == "__main__":
  bot.run(os.getenv['DISCORD_TOKEN'])
