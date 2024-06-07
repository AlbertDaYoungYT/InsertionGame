

class TriggerZone(object):

    def __init__(self, observer, observable, callback):
        self.observer = observer
        self.observable = observable
        self.callback = callback
    