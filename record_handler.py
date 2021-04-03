import json
from time import time_ns
from math import inf

class RecordHandler():
    def __init__(self):
        try:
            with open("records.json") as f:
                self.datas = json.load(f)
        except:
            with open("records.json",'w+') as f:
                self.datas = {"metadata":{"count":{},"best":{},"average":{}},"datas":{}}
                f.write(str(self.datas))

    def update(self, mode:str, time:float, date:float, comment:str=""):
        
        if not (mode in self.datas["metadata"]["count"].keys()):
            #FIRST TIME
            if time == inf:
                self.datas["metadata"]["count"][mode] = 0
                self.datas["metadata"]["best"][mode] = inf
                self.datas["metadata"]["average"][mode] = 0
            else:
                self.datas["metadata"]["count"][mode] = 1
                self.datas["metadata"]["best"][mode] = time
                self.datas["metadata"]["average"][mode] = time
            
            self.datas["datas"][mode] = []
        else:
            #DATA EXISTS
            
            if time != inf:
                avg = self.datas["metadata"]["average"][mode]
                c = self.datas["metadata"]["count"][mode]

                self.datas["metadata"]["count"][mode] += 1
                self.datas["metadata"]["best"][mode] = min(time,self.datas["metadata"]["best"][mode])
                self.datas["metadata"]["average"][mode] = (avg * c + time) / (c + 1)
        
        self.datas["datas"][mode].append([{"date":date, "time":time, "comment":comment}])

    def average(self, mode, n):
        if len(self.datas["datas"][mode]) < n:
            return None
        else:
            l = len(self.datas["datas"][mode])
            times = [self.datas["datas"][mode][i][0]["time"] for i in range(l-n, l)]
        
        times.remove(min(times))
        times.remove(max(times))
        return sum(times)/(n-2)

    def close(self):
        print("dumping")
        with open("records.json","w+") as f:
            json.dump(self.datas, f, indent = 4)

if __name__ == "__main__":
    handler = RecordHandler()
    for x,y in enumerate([11,"dnf",17]):
        handler.update("3x3", y)
    handler.close()