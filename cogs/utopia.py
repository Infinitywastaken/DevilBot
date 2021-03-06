import discord
from discord.ext import commands
import json, random

class utopiaCog(commands.Cog):
    """Utopian-only commands"""

    def __init__(self, bot):
        self.bot = bot
        self.db_conn = bot.db_conn
        self.colour = 0xff9300
        self.footer = 'Bot developed by DevilJamJar#0001\nWith a lot of help from ♿nizcomix#7532'
        self.thumb = 'https://styles.redditmedia.com/t5_3el0q/styles/communityIcon_iag4ayvh1eq41.jpg'

    async def cog_check(self, ctx):
        return ctx.guild.id == 621044091056029696

    @commands.command()
    async def nominate(self, ctx, message:discord.Message):
        with open('nominees.json', 'r') as f:
            nominees = json.load(f)
        nominees[f'{str(message.clean_content)}∫√∆{str(message.author)}∫√∆{str(message.created_at)}'] = str(message.id)
        with open('nominees.json', 'w') as f:
            json.dump(nominees, f, indent=4)
        await ctx.send(f'{ctx.author.mention}, successfully inserted message into nominations. Use {ctx.prefix}utopiaquote for a random one!')

    @commands.command(aliases=['uq', 'utopiaq', 'uquote'])
    async def utopiaquote(self, ctx):
        full=[]
        with open('nominees.json', 'r') as f:
            nominees = json.load(f)
        for i in nominees:
            full.append(i)
        final = random.choice(full).split('∫√∆')
        embed=discord.Embed(
            colour = self.colour,
            description=f'**Message:**\n{final[0]}\n**Author:**\n{final[1]}\n**Created At:**\n{final[2]}'
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(utopiaCog(bot))