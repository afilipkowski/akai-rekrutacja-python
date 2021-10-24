import json


class Importer:
    jlist = []

    def __init__(self):
        self.jlist=[]

    def read_tasks(self):
        jfile = open("taski.json", "r", encoding="utf-8")
        self.jlist = json.load(jfile)
        

    def get_tasks(self):
        return self.jlist