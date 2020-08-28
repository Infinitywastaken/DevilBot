import discord
from discord.ext import commands
import secrets

import asyncpraw, random, aiohttp

reddit = asyncpraw.Reddit(client_id=secrets.secrets_asyncpraw_client_id,
                          client_secret=secrets.secrets_asyncpraw_client_secret,
                          password=secrets.secrets_asyncpraw_password,
                          user_agent=secrets.secrets_asyncpraw_user_agent,
                          username=secrets.secrets_asyncpraw_username)

class redditCog(commands.Cog):
    """Reddit commands"""

    def __init__(self, bot):
        self.bot = bot
        self.db_conn = bot.db_conn
        self.colour = 0xff9300
        self.footer = 'Bot developed by DevilJamJar#0001\nWith a lot of help from ♿nizcomix#7532'
        self.thumb = 'https://styles.redditmedia.com/t5_3el0q/styles/communityIcon_iag4ayvh1eq41.jpg'

    # Code used from niztg's CyberTron5000 GitHub Repository Provided by the MIT License
    # https://github.com/niztg/CyberTron5000/blob/master/CyberTron5000/cogs/reddit.py#L83-L105
    # Copyright (c) 2020 niztg

    @commands.command(aliases=['maymay'])
    async def meme(self, ctx):
        subreddit = random.choice(
            [
                'memes', 'dankmemes', 'dankexchange', 'okbuddyretard', 'wholesomememes'
            ]
        )
        memes=[]
        async with ctx.typing():
            subreddit = await reddit.subreddit(subreddit)
            async for submission in subreddit.hot(limit=50):
                if not submission.over_18 and not submission.distinguished and not submission.is_self:
                    memes.append(submission)
        submission = random.choice(memes)
        embed=discord.Embed(
                colour=self.colour,
                title=submission.title.capitalize(),
                url=f'https://reddit.com{submission.permalink}',
                description=f'Posted in r/{subreddit} by u/{submission.author.name}\n\n\
                              <:upvote:748924744572600450> {submission.score}'
            )
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(redditCog(bot))
