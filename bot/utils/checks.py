from discord.ext import commands

class check():
  def __init__(self):
    self.bot_id = 1027961443687075860
    self.owner_id = 686588183496097793

  def is_owner(self):
    async def predicate(ctx):
      return ctx.author.id == self.owner_id
    return commands.check(predicate)

  def is_bot(self):
    async def predicate(ctx):
      return ctx.author.id == self.bot_id
    return commands.check(predicate)

  def grab_id(self):
    return self.bot_id