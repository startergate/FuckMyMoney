import threading
import asyncio
import json
import requests


@asyncio.coroutine
async def steamLibraryConnectivity(steamid=76561198149890990):
    while True:
        userlib = requests.get(
            'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=B6137C92F67299965B5E6BF287ECA4AE&steamid={}&include_appinfo=1&format=json'.format(
                steamid))
        userlib = userlib.json()
        try:
            games = userlib['response']['games']
        except:
            print(userlib)
            continue
        print(games)
        with open('data/data.json', 'w+') as output:
            json.dump(games, output)
        await asyncio.sleep(100)


def infiniteLoop():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(steamLibraryConnectivity(76561198149890990))


t = threading.Thread(target=infiniteLoop)
t.daemon = True
t.start()
