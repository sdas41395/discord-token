import discord
import json
import random
from discord.ext import commands

token_dict = {}

bot = commands.Bot(command_prefix='/')

@bot.command(name='list')
async def _list(ctx):
    for user in token_dict:
        await ctx.send('User {} has {} coins'.format(user, token_dict[user]))

@bot.event
async def on_ready():   
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Randomly award tokens
    token_percent = random.randrange(1, 99)
    if token_percent > 25:
        token_amount = random.randrange(1, 99)
        if str(message.author) not in token_dict:
            token_dict[str(message.author)] = token_amount
        else:
            token_dict[str(message.author)] += token_amount
        json_token = json.dumps(token_dict)

    await bot.process_commands(message)
    # await message.channel.send(f"You have been awarded {token_amount} tokens!")
    # await message.channel.send(f"Current Ranking: {json_token}")
    return

bot.run('')
