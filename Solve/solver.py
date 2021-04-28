import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))

import numpy as np
import kociemba
from GL.cube import Cube



class Solve:
    def __init__(self, cube):
        self.attach(cube)
        self._parser()

    def attach(self, cube):
        self.cube = cube
        self.state = self.cube.sides

    def solve(self):
        return kociemba.solve(self._parsed_state)

    def pattern_solve(self, final_state):
        return kociemba.solve(self._parsed_state, self._parser(final_state))

    def _parser(self, final_state=None):
        
        [a,b,c,d,e,f] = self.state if not final_state else final_state.state
        sides = np.array([a,c,e,b,d,f]).reshape(-1)
        
        self._parsed_state = ""
        for elem in sides:
            self._parsed_state += elem            

a = Cube(3)
slv = Solve(a)
print(slv.solve())