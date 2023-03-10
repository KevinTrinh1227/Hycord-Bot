import discord
from discord.ext import commands
import discord.ui
import datetime
import json

# Open the JSON file and read in the data
with open('config.json') as json_file:
    data = json.load(json_file)

embed_color = data["embed_color"]
embed_color = int(data["embed_color"].strip("#"), 16) #convert hex color to hexadecimal format

#reaction roles
class Roles(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
    @discord.ui.button(label = "đī¸", custom_id = "Role 1", style = discord.ButtonStyle.secondary)
    async def button1(self, interaction, button):
        role = 934424403150766150
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()
    @discord.ui.button(label = "đĄī¸", custom_id = "Role 2", style = discord.ButtonStyle.secondary)
    async def button2(self, interaction, button):
        role = 1054991878841446450
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()
    @discord.ui.button(label = "âī¸", custom_id = "Role 9", style = discord.ButtonStyle.secondary)
    async def button9(self, interaction, button):
        role = 1054991871493033994
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()
    @discord.ui.button(label = "đšī¸", custom_id = "Role 10", style = discord.ButtonStyle.secondary)
    async def button10(self, interaction, button):
        role = 1054991881420931122
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()
    @discord.ui.button(label = "đ", custom_id = "Role 7", style = discord.ButtonStyle.secondary)
    async def button7(self, interaction, button):
        role = 934424365020360714
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()
    @discord.ui.button(label = "đĢ ", custom_id = "Role 6", style = discord.ButtonStyle.secondary)
    async def button6(self, interaction, button):
        role = 1054991883937521734
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()
    @discord.ui.button(label = "đ", custom_id = "Role 5", style = discord.ButtonStyle.secondary)
    async def button5(self, interaction, button):
        role = 1054991875330801744
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()
    @discord.ui.button(label = "đŦ", custom_id = "Role 3", style = discord.ButtonStyle.secondary)
    async def button3(self, interaction, button):
        role = 934424330765471764
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()
    @discord.ui.button(label = "đą", custom_id = "Role 4", style = discord.ButtonStyle.secondary)
    async def button4(self, interaction, button):
        role = 934424304379125850
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()
    @discord.ui.button(label = "đŧ", custom_id = "Role 8", style = discord.ButtonStyle.secondary)
    async def button8(self, interaction, button):
        role = 934424272758247436
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.defer()
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.defer()


class selfroles(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.has_permissions(administrator = True)
    @commands.command(aliases = ["sr", "serverroles"], brief="roles", description="Print menu for self selecting roles.")
    async def roles(self, ctx):
        serverIconLink = ctx.guild.icon.url
        embed = discord.Embed(
            title = "**PUBLIC SELF SELECTION ROLES**",
            description = "Use the following menu below to chose your own personal roles. \n\n<@&934424403150766150>  â Classify as a Bedwars player\n<@&1054991878841446450> â classify as a Skywars player \n<@&1054991871493033994> â Classify as a Duels Practice player \n<@&1054991881420931122> â Classify as a Arcade Games player\n\n<@&934424365020360714> â Get pinged for Bedwars parties\n<@&1054991883937521734> â Get pinged for general squads\n<@&1054991875330801744> â Get pinged for community game nights\n\n<@&934424330765471764> â Classify as age 20+\n<@&934424304379125850> â Classify within age group 17 - 19\n<@&934424272758247436> â Classify within the age group 13 - 16 \n\nClick on the corresponding buttons to claim or unclaim a role. Note that roles can always be claimed/unclaimed.\n",
            color = embed_color
        )
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=f"ÂŠī¸ {ctx.guild.name}", icon_url = serverIconLink)
        await ctx.channel.purge(limit = 1)
        await ctx.send(embed = embed, view = Roles())
        
        
        
    @roles.error
    async def ban_error(self, ctx, error):
        #if user does not have the permission node
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color = embed_color
            )
            embed.timestamp = datetime.datetime.now()
            embed.set_image(url="https://imgur.com/nU9QbXv.png")
            embed.set_footer(text = f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
            await ctx.send(embed=embed)
        #if the command was missing arguments
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color = embed_color
            )
            embed.timestamp = datetime.datetime.now()
            embed.set_image(url="https://imgur.com/tQzEKFv.png")
            embed.set_footer(text = f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
            await ctx.send(embed=embed)
        #other error
        else:
            print(error) # for other errors so they dont get suppressed
        
        
async def setup(client):
    client.add_view(Roles())
    await client.add_cog(selfroles(client))