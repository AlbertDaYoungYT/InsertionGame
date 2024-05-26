import termux
import sys


class TermuxAPI:

    def __init__(self):
        self.isTermuxAvalible = None
        self.requirements = {bool(hasattr(sys, "getandroidapilevel")): True}
    

    def load(self):
        req_list = []
        for k, v in self.requirements:
            if k == v:
                req_list.append(k == v)

        if False in req_list: return 2

        return 1
