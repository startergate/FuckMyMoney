import threading
import asyncio
import requests


def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()


def steamLibraryConnectivity(id):
    pass
