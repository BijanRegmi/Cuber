import time

class Time_calc():
    def __init__(self):
        self.state = 0          #0==>stopped    1==>running     -1==>paused
        self.initial = 0
        self.final = 0
        self.elapsed = 0

    def start(self):
        self.state = 1
        self.initial = time.time_ns()

    def pause(self):
        curr = time.time_ns()
        if self.state == 1:
            self.elapsed += curr - self.initial
        elif self.state == -1:
            self.initial = curr
        self.state *= -1
        return self.elapsed
        
    def reset(self):
        self.__init__()

    def parser(self, val):
        val = str(val)
        res = ""
        for i in range(6):
            try:
                res = val[-8 - i] + res
            except:
                res = "0" + res
        t_s = int(res[0:4])
        minu = str(t_s // 60).zfill(2)
        sec = str(t_s % 60).zfill(2)
        return minu + sec + res[4:6]

if __name__ == "__main__":
    tim = Time_calc()

    tim.start()
    
    time.sleep(3)
    
    el = tim.pause()
    
    tim.reset()
    
    print(el)
