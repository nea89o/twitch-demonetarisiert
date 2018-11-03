from threading import Thread
from time import sleep

from .config import config
from .irc import Client

connection = Client()


def send_msg():
    connection.ready.wait()
    while True:
        connection.connection.privmsg("#" + config.channel, "#familyfriendly, bitte!")
        sleep(300)


def main():
    t = Thread(target=send_msg)
    t.start()
    connection.setup()
