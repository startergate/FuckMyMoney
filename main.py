import discord
import requests
import setting
import modules.steamSync as steam

app = discord.Client()

token = setting.TOKEN


@app.event
async def on_ready():
    print("Logged In as:")
    print(app.user.name)
    print(app.user.id)
    print("=============")

    await app.change_presence(activity=discord.Game("Steam: Buy More Useless Games!"))


@app.event
async def on_message(message):
    if message.author.bot:
        return None
    msg = message.content
    if msg == "남고생쟝 초대하기":
        await message.channel.send(embed=discord.Embed(title="남고생쟝의 친구가 되어주세요!", description=discord.utils.oauth_url(app.user.id, discord.Permissions(67584))))
        return None
    if bool(msg):
        if "some string" in msg:
            with open('static/ShootingFrog.png', 'rb') as shit_postingFrog:
                await message.channel.send(file=discord.File(shit_postingFrog, 'file.png'))

app.run(token)
