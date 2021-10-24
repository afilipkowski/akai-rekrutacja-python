import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        jfile = open("taski.json", "w", encoding="utf-8")
        json.dump(tasks, jfile, indent=4)
        jfile.close()
        
