import time
import logging
import win32api, win32con
import socket #imports module allowing connection to IRC
import threading #imports module allowing timing functions
from emoji import demojize

#sets variables for connection to twitch chat
bot_owner = "TwitchBot"
nick = "sirsnufflez"
channel = "#sirsnufflez"
server = "irc.chat.twitch.tv"
password = "" 
PORT = 6667

irc = socket.socket()
irc.connect((server, PORT)) #connects to the server

irc.send(f"PASS {password}\n".encode('utf-8'))
irc.send(f"NICK {nick}\n".encode('utf-8'))
irc.send(f"JOIN {channel}\n".encode('utf-8'))

resp = irc.recv(2048).decode('utf-8')
print(resp)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])
logging.info(resp)

while True:
    resp = irc.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        irc.send("PONG\n".encode('utf-8'))
    
    elif len(resp) > 0:
        logging.info(demojize(resp))
