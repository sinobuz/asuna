import os
import discord
from keep_alive import keep_alive
from discord.ext import commands


client = commands.Bot(command_prefix = 'a.', intents=discord.Intents.default())
client.remove_command('help')

@client.event 
async def on_ready():
  print("Asuna Online. Link Start!")
  print(client.user)
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Bot Version: 0.5.0 Alpha | a.support or a.help'))

@client.command()
async def support(ctx):
    embed=discord.Embed(title="**Get Support Now!**", url="https://discord.gg/x", description="Join the official Asuna Server to get help, report errors, or get access to features no one else can!", color=0xFF0000)
    embed.set_author(name="Asuna", icon_url=client.user.avatar_url)
    embed.add_field(name="Support Server", value="https://discord.gg/x", inline=True)
    embed.add_field(name="Help Command", value="a.help", inline=True)
    await ctx.send(embed=embed)

@client.command()
async def botinfo(ctx):
    embed=discord.Embed(title="Bot Information", description="Information on the bot Asuna", color=0xFF0000)
    embed.set_author(name="Asuna", icon_url=client.user.avatar_url)
    embed.add_field(name="Bot Version", value="0.5.0", inline=False)
    embed.add_field(name="Bot Prefix", value="a.", inline=False)
    embed.add_field(name="Coding Language/Library", value="discord.py/Python", inline=False)
    embed.add_field(name="Github Repository", value="https://github.com/ashdsc/asuna", inline=False)
    embed.add_field(name="Bot Creator", value="ashdsc", inline=False)
    embed.set_footer(text="Asuna BotInfo", icon_url=client.user.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def premium(ctx):
    embed=discord.Embed(title="Asuna Premium", description="Are you thinking about buying Asuna Premium? Here are some reasons you should buy it!", color=0xFF0000)
    embed.set_author(name="Asuna", icon_url=client.user.avatar_url)
    embed.add_field(name="Get Access To More Commands", value="You can access tons of commands, from advanced roleplay, to 24/7 music!", inline=False)
    embed.add_field(name="Beta Testing", value="Asuna Premium will update the quickest. You will have access to new commands a week before normal Asuna users!", inline=False)
    embed.add_field(name="Name in Command", value="Your name will be added to a Google Document of Premium users that is connected to a command that everyone can use!", inline=False)
    embed.add_field(name="Premium role in Discord Server", value="You will get a Premium role in our support Discord server, which can be found by running **a.support**!", inline=False)
    embed.add_field(name="Are you interested?", value="Join our support server and leave a message in the channel called *premium-reqs*, a staff will get to you as soon as they can.", inline=False)
    embed.set_footer(text="Asuna Premium", icon_url=client.user.avatar_url)
    await ctx.send(embed=embed)

@client.command(description="Mutes the specified user.")
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")

  if not mutedRole:
    mutedRole = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False)
  await member.add_roles(mutedRole, reason=reason)
  await ctx.send(f"Muted {member} for reason {reason}")
  await member.send(f"You were muted in {member.guild.name} for {reason}")

@client.command(description="Unmutes the specified user.")
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")

  await member.remove_roles(mutedRole)
  await ctx.send(f" {member} was unmuted successfully.")
  await member.send(f"You were unmuted in {member.guild.name}.")

@client.command()
async def ping(ctx):
  latency = round(client.latency * 1000, 1)
  await ctx.send(f"Pong! {latency}ms")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f"{member} was banned successfully.")
  await member.send(f"You got banned in {member.guild.name} because {reason}")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f"{member} was kicked successfully.")
  await member.send(f"You got kicked in {member.guild.name} because {reason}")

@client.command(name='avatar', aliases=['Avatar', 'av'])
async def av_cmd(ctx, user: discord.Member):
	mbed = discord.Embed(
		color = discord.Color(0xffff),
		title=f"{ctx.author}"

	)
	mbed.set_image(url=f"{user.avatar_url}")
	await ctx.send(embed=mbed)


@av_cmd.error
async def avatar_error(ctx, error):
	if isinstance (error, commands.MissingRequiredArgument):
		mbed = discord.Embed(
			color = discord.Color(0xffff),
			title=f"{ctx.author}"
		
		)
		mbed.set_image(url=f"{ctx.author.avatar_url}")
		await ctx.send(embed=mbed)


@client.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)


extensions = ['Cogs.help']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

keep_alive()
token = os.environ.get("token")
client.run(token)
