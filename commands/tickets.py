import discord
from discord.ext import commands
import discord.ui
import datetime
import json
import asyncio
import io
import chat_exporter

# Open the JSON file and read in the data
with open('config.json') as json_file:
    data = json.load(json_file)

embed_color = data["embed_color"]
embed_color = int(data["embed_color"].strip("#"), 16) #convert hex color to hexadecimal format
bot_prefix = data["bot_prefix"]

category_id = int(data["tickets_category_id"])
staff_role_id = int(data["staff_member_role_id"])
transcript_channel_id = int(data["tickets_trascripts_channel_id"])
bots_role_id = int(data["bots_role_id"])

class Roles(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    #button 1
    @discord.ui.button(label="🔨", custom_id="ticket 1", style = discord.ButtonStyle.secondary)
    async def create_ticket1(self, interaction, button):
        guild = interaction.guild
        category = guild.get_channel(category_id)
        staff_role = guild.get_role(staff_role_id)
        user = interaction.user

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            staff_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channel = await category.create_text_channel(f'ticket-{user.name}-🔨', overwrites=overwrites)

        ticket_type = "🔨 Reporting A Cheater"

        role_id = staff_role_id #staff member role ID
        staff_role = guild.get_role(role_id)
        await channel.send(f"||{staff_role.mention}{user.mention}||")
        await channel.purge(limit = 1)

        embed = discord.Embed(
            title = f"**{ticket_type} Ticket**",
            description = f"Please describe your issue clearly and a staff member will assist you shortly. Be sure to provide any attachments if nescessay.\n\nTicket Issuer: {user.mention}\n\nUse the command `{bot_prefix}close` to close this ticket.",
            color = embed_color
        )
        embed.set_author(name=f"Requested by {user}", icon_url=user.avatar.url),
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url="{}".format(guild.icon.url)),
        embed.set_footer(text=f"©️ {guild.name}", icon_url = guild.icon.url)
        await channel.send(embed = embed)
        await interaction.response.defer()

    # button 2
    @discord.ui.button(label="🫂", custom_id="ticket 2", style=discord.ButtonStyle.secondary)
    async def create_ticket2(self, interaction, button):
        guild = interaction.guild
        category = guild.get_channel(category_id)
        staff_role = guild.get_role(staff_role_id)
        user = interaction.user

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            staff_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channel = await category.create_text_channel(f'ticket-{user.name}-🫂', overwrites=overwrites)

        ticket_type = "🫂 Applying for staff"

        role_id = staff_role_id  # staff member role ID
        staff_role = guild.get_role(role_id)
        await channel.send(f"||{staff_role.mention}{user.mention}||")
        await channel.purge(limit=1)

        embed = discord.Embed(
            title=f"**{ticket_type} Ticket**",
            description=f"Please describe your issue clearly and a staff member will assist you shortly. Be sure to provide any attachments if nescessay.\n\nTicket Issuer: {user.mention}\n\nUse the command `{bot_prefix}close` to close this ticket.",
            color=embed_color
        )
        embed.set_author(name=f"Requested by {user}", icon_url=user.avatar.url),
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url="{}".format(guild.icon.url)),
        embed.set_footer(text=f"©️ {guild.name}", icon_url=guild.icon.url)
        await channel.send(embed=embed)
        await interaction.response.defer()
    # button 3
    @discord.ui.button(label="📮", custom_id="ticket 3", style=discord.ButtonStyle.secondary)
    async def create_ticket3(self, interaction, button):
        guild = interaction.guild
        category = guild.get_channel(category_id)
        staff_role = guild.get_role(staff_role_id)
        user = interaction.user

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            staff_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channel = await category.create_text_channel(f'ticket-{user.name}-📮', overwrites=overwrites)

        ticket_type = "📮 Requesting Role(s)"

        role_id = staff_role_id  # staff member role ID
        staff_role = guild.get_role(role_id)
        await channel.send(f"||{staff_role.mention}{user.mention}||")
        await channel.purge(limit=1)

        embed = discord.Embed(
            title=f"**{ticket_type} Ticket**",
            description=f"Please describe your issue clearly and a staff member will assist you shortly. Be sure to provide any attachments if nescessay.\n\nTicket Issuer: {user.mention}\n\nUse the command `{bot_prefix}close` to close this ticket.",
            color=embed_color
        )
        embed.set_author(name=f"Requested by {user}", icon_url=user.avatar.url),
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url="{}".format(guild.icon.url)),
        embed.set_footer(text=f"©️ {guild.name}", icon_url=guild.icon.url)
        await channel.send(embed=embed)
        await interaction.response.defer()
    # button 4
    @discord.ui.button(label="🔥", custom_id="ticket 4", style=discord.ButtonStyle.secondary)
    async def create_ticket4(self, interaction, button):
        guild = interaction.guild
        category = guild.get_channel(category_id)
        staff_role = guild.get_role(staff_role_id)
        user = interaction.user

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            staff_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channel = await category.create_text_channel(f'ticket-{user.name}-🔥', overwrites=overwrites)

        ticket_type = "🔥 Applying for guild"

        role_id = staff_role_id # staff member role ID
        staff_role = guild.get_role(role_id)
        await channel.send(f"||{staff_role.mention}{user.mention}||")
        await channel.purge(limit=1)

        embed = discord.Embed(
            title=f"**{ticket_type} Ticket**",
            description=f"Please describe your issue clearly and a staff member will assist you shortly. Be sure to provide any attachments if nescessay.\n\nTicket Issuer: {user.mention}\n\nUse the command `{bot_prefix}close` to close this ticket.",
            color=embed_color
        )
        embed.set_author(name=f"Requested by {user}", icon_url=user.avatar.url),
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url="{}".format(guild.icon.url)),
        embed.set_footer(text=f"©️ {guild.name}", icon_url=guild.icon.url)
        await channel.send(embed=embed)
        await interaction.response.defer()
    # button 5
    @discord.ui.button(label="🔍", custom_id="ticket 5", style=discord.ButtonStyle.secondary)
    async def create_ticket5(self, interaction, button):
        guild = interaction.guild
        category = guild.get_channel(category_id)
        staff_role = guild.get_role(staff_role_id)
        user = interaction.user

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            staff_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channel = await category.create_text_channel(f'ticket-{user.name}-🔍', overwrites=overwrites)

        ticket_type = "🔍 Other (Not Listed Category)"

        role_id = staff_role_id  # staff member role ID
        staff_role = guild.get_role(role_id)
        await channel.send(f"||{staff_role.mention}{user.mention}||")
        await channel.purge(limit=1)

        embed = discord.Embed(
            title=f"**{ticket_type} Ticket**",
            description=f"Please describe your issue clearly and a staff member will assist you shortly. Be sure to provide any attachments if nescessay.\n\nTicket Issuer: {user.mention}\n\nUse the command `{bot_prefix}close` to close this ticket.",
            color=embed_color
        )
        embed.set_author(name=f"Requested by {user}", icon_url=user.avatar.url),
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url="{}".format(guild.icon.url)),
        embed.set_footer(text=f"©️ {guild.name}", icon_url=guild.icon.url)
        await channel.send(embed=embed)
        await interaction.response.defer()

class Ticket(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.category_id = category_id  # Replace with your desired category ID
        self.staff_role_id = staff_role_id  # Replace with your staff role ID

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=["tickets", "t"], brief="ticket", description="Activates ticket system.")
    async def ticket(self, ctx):
        await ctx.channel.purge(limit=1)
        serverIconLink = ctx.guild.icon.url
        embed = discord.Embed(
            title = f"**{ctx.guild.name} Support**",
            description = "Require Support? Click a button below with the corresponding category's emoji and a private channel will be created where our staff team will be ready to assist you!\n\n **Categories**\n🔨 Report a cheater\n🫂 Apply for staff\n📮 Request a role(s)\n🔥 Apply for guild\n🔍 Other \n\nPlease be patient with our staff team, and remember that any abuse of our ticket system will result in a punishment.",
            color = embed_color
        )
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url="{}".format(ctx.guild.icon.url)),
        embed.set_footer(text=f"©️ {ctx.guild.name}", icon_url = serverIconLink)
        await ctx.send(embed = embed, view = Roles())

    @commands.command(aliases=["close"], brief="close", description="Closes the current ticket")
    async def close_ticket(self, ctx):
        if not ctx.channel.name.startswith("ticket-"):
            #await ctx.send("This command can only be used in a ticket channel.")
            pass
            return

        # Create a confirmation message
        embed = discord.Embed(
            title="Confirmation",
            description="Are you sure that you want to close your ticket? If so please click on the reaction below this message. Otherwise please ignore this message.",
            colour=embed_color
        )
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=f"©️ {ctx.guild.name}", icon_url = ctx.guild.icon.url)
        confirm_msg = await ctx.send(embed=embed)

        # Add a checkmark reaction to the message
        await confirm_msg.add_reaction("✅")

        # Wait for the author to react with a checkmark
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "✅" and reaction.message == confirm_msg

        try:
            reaction, user = await self.client.wait_for("reaction_add", timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Confirmation timed out. Ticket will not be closed. Run the command again to close.")
            return

            
        #saving the channel as a html
        transcript = await chat_exporter.export(ctx.channel)
        if transcript is None:
            return

        transcript_file = discord.File(
            io.BytesIO(transcript.encode()),
            filename=f"transcript-{ctx.channel.name}.html",
        )

        transcript_channel = self.client.get_channel(transcript_channel_id)
        message = await transcript_channel.send(file=transcript_file)
        link = await chat_exporter.link(message)
        #await ctx.send("Click this link to view the transcript online: " + link)
        
        
        #sends this embed message to a staff only chat as a record
        embed3 = discord.Embed(
            title="Ticket Closed",
            url=link,
            description="A ticket has been closed, below is a link to the transcript.",
            colour=embed_color
        )
        embed3.timestamp = datetime.datetime.now()
        embed3.set_footer(text=f"©️ {ctx.guild.name}", icon_url = ctx.guild.icon.url)
        embed3.add_field(
            name="Closed By",
            value=f"{ctx.author}"
        )
        embed3.add_field(
            name="View transcript",
            value=f"[Click here to view the transcript]({link})"
        )
        
        
        #sends this embed message to the ticket channel
        embed2 = discord.Embed(
            title="Closed | This ticket is now locked",
            url=link,
            description="Your support ticket is now locked. If you wish to keep a record of this ticket, please use the link provided below to view the transcript online and save it in your files.\n\n***This channel will be terminated in 1 minute.\n\n***",
            colour=embed_color
        )
        #embed2.set_author(name = f"Closed by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed2.timestamp = datetime.datetime.now()
        embed2.set_footer(text=f"©️ {ctx.guild.name}", icon_url = ctx.guild.icon.url)
        embed2.add_field(
            name="Closed By",
            value=f"{ctx.author}"
        )
        embed2.add_field(
            name="View transcript",
            value=f"[Click here to view the transcript]({link})"
        )
        
        # to avoid being rate limited, it only affects users without the following roles...
        role_ids = [bots_role_id, staff_role_id] #bot role, staff member role
        
        #deleting message above
        await ctx.channel.purge(limit=1)
        
        #sending both embed messages to the channels...
        await ctx.send(embed=embed2)
        await transcript_channel.send(embed=embed3)

        # Revoke the send messages permission for every user in the channel who doesn't have the specified roles
        for member in ctx.channel.members:
            if not any(role.id in role_ids for role in member.roles):
                await ctx.channel.set_permissions(member, send_messages=False, read_messages=True)

        
        #wait a minute before deleting channel
        await asyncio.sleep(60)  # Wait for 20 seconds before deleting the channel
        await ctx.channel.delete()

async def setup(client):
    client.add_view(Roles())
    await client.add_cog(Ticket(client))
