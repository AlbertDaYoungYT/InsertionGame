import threading
import requests


class Server(threading.Thread):

    def __init__(self, _self):
        self.__init__(_self)
        threading.Thread.__init__(self)

        self.server_uri = "https://"

        self.get = requests.get
        self.post = requests.post

    
    def checkForUpdates(self):
        res = self.get(self.server_uri)