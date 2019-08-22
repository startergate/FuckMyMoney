import threading
import asyncio
import json
import requests

games = None


@asyncio.coroutine
async def steamLibraryConnectivity(steamid=76561198149890990):
    global games
    while True:
        userlib = requests.get(
            'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=B6137C92F67299965B5E6BF287ECA4AE&steamid={}&include_appinfo=1&format=json'.format(
                steamid))
        userlib = userlib.json()
        try:
            games = userlib['response']['games']
        except:
            continue
        await asyncio.sleep(100)


def infiniteLoop():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(steamLibraryConnectivity(76561198149890990))


t = threading.Thread(target=infiniteLoop)
t.daemon = True
t.start()
