from threading import Event as TEvent

from irc.client import SimpleIRCClient, ServerConnection, Event

from .config import config

SERVER = "irc.chat.twitch.tv"
PORT = 6667
CHANNEL = "#" + config.channel
NICK = config.name


class Client(SimpleIRCClient):
    def __init__(self):
        super().__init__()
        self.ready = TEvent()

    def setup(self):
        self.connect(SERVER, PORT, NICK, password=config.password)
        self.start()

    def on_endofmotd(self, conn: ServerConnection, event: Event):
        print('Well, we are done here.')
        conn.join(CHANNEL)

    def on_motd(self, conn: ServerConnection, event: Event):
        print("Motd: " + event.arguments[0])

    def on_pubmsg(self, conn: ServerConnection, event: Event):
        if event.arguments[0] == 'test123':
            conn.privmsg(CHANNEL, '#familyfriendly, bitte!')

    def on_endofnames(self, conn: ServerConnection, event: Event):
        self.ready.set()

    def _dispatcher(self, conn: ServerConnection, event: Event):
        if event.type != 'all_raw_messages':
            print(event)
        super(Client, self)._dispatcher(conn, event)
