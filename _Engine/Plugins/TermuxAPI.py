import termux
import json
import sys


class TermuxAPI:
    class InternalAPI(object):

        def __init__(self):
            self.t = termux.API

        def battery(self):
            return json.loads(self.t.battery())

        def vibrate(self, d, force=True):
            return json.loads(self.t.vibrate(duration=d, force=force))
        
        def notify(self, t, c, id, *args, **kwargs):
            return json.loads(self.t.Notification.notify(title=t, content=c, nid=id, *args, **kwargs))
        
        def deleteNotifier(self, id):
            return json.loads(self.t.Notification.remove(nid=id))
        
        def wakeLock(self): return json.loads(self.t.Wake.lock())
        
        def wakeUnlock(self): return json.loads(self.t.Wake.unlock())


    def __init__(self):
        self.isTermuxAvalible = None
        self.requirements = {bool(hasattr(sys, "getandroidapilevel")): True}

        self.isTermuxAvalible = True if self.load() == 1 else False
        if self.isTermuxAvalible:
            self.API = self.InternalAPI
    

    def load(self):
        req_list = []
        for k, v in self.requirements:
            if k == v:
                req_list.append(k == v)

        if False in req_list: return 2

        return 1