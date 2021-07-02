import discord
from discord.ext import commands
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Help cog successfully loaded.")
    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(title="Trackpad Help", description="", color=discord.Colour.green())
        em.description += f"**a.modhelp**: Learn the **moderation** based commands."
        em.description += f"\n**a.funhelp**: Learn the **fun or interactive** based commands."
        em.description += f"\n**a.support**: **Get support with Asuna.**"
        em.set_footer(text="Asuna", icon_url=self.client.user.avatar_url)



        await ctx.send(embed=em)
    @commands.command()
    async def modhelp(self, ctx):
        emb = discord.Embed(title="Moderation Help", description="", color=discord.Colour.green())
        emb.description += f"\n**a.kick**: Automatically removes someone from the guild."
        emb.description += f"\n**a.mute**: Gives a user a role that makes them unable to talk."
        emb.description += f"\n**a.ban** : Removes a user from the guild and makes them unable to join back."
        emb.description += f"\n**a.unmute**: Makes a user that was muted able to talk again."
        await ctx.send(embed=emb)
def setup(client):
  client.add_cog(Help(client))

