import numpy as np

class Cube:
    faces = {"U":0,"D":1,"R":2,"L":3,"F":4,"B":5}
    surr = {
            "U":"5243",
            "R":"0514",
            "F":"0213",
        }
    
    def __init__(self, length):
        self.length = length
        self.sides = np.array([np.tile((list(self.faces.keys())[i]),(self.length, self.length)) for i in range(6)])        

    def move(self, layer, depth, angle):
        if layer in ["F", "U", "R"] and depth<=self.length:
            if depth == 1:
                self.sides[self.faces[layer]] = self._rotate(self.sides[self.faces[layer]], angle)
            elif depth == self.length:
                self.sides[self.faces[layer]+1] = self._rotate(self.sides[self.faces[layer]+1], -angle)
            roll_mat = self._get_roll_mat(layer, depth)
            roll_mat = np.roll(roll_mat,self.length*(angle//90))
            self._set_back_roll(roll_mat,layer,depth)
        
        else:
            if layer == "B":
                self.move("F", self.length-depth+1, -angle)
            elif layer == "D":
                self.move("U", self.length-depth+1, -angle)
            elif layer == "L":
                self.move("R", self.length-depth+1, -angle)

    def _set_back_roll(self, roll_mat, layer, depth):
        n = self.length
        d = depth
        surr_layers = self.surr[layer]
        e,f,g,h = np.split(roll_mat,4)
        
        if layer == "F":
            self.sides[int(surr_layers[0])][n-d,:] = e
            self.sides[int(surr_layers[1])][:,d-1] = f
            self.sides[int(surr_layers[2])][d-1,:][::-1] = g
            self.sides[int(surr_layers[3])][:,n-d][::-1] = h
        elif layer == "U":
            self.sides[int(surr_layers[0])][d-1,:] = e
            self.sides[int(surr_layers[1])][d-1,:] = f
            self.sides[int(surr_layers[2])][d-1,:] = g
            self.sides[int(surr_layers[3])][d-1,:] = h
        elif layer == "R":
            self.sides[int(surr_layers[0])][:,n-d][::-1] = e
            self.sides[int(surr_layers[1])][:,d-1] = f
            self.sides[int(surr_layers[2])][:,n-d][::-1] = g
            self.sides[int(surr_layers[3])][:,n-d][::-1] = h



    def _get_roll_mat(self, layer, depth):
        n = self.length
        d = depth
        surr_layers = self.surr[layer]
        e,f,g,h = [self.sides[int(i)] for i in surr_layers]
        
        if layer == "F":
            e = e[n-d,:]
            f = f[:,d-1]
            g = g[d-1,:][::-1]
            h = h[:,n-d][::-1]
        elif layer == "U":
            e = e[d-1,:]
            f = f[d-1,:]
            g = g[d-1,:]
            h = h[d-1,:]
        elif layer == "R":
            e = e[:,n-d][::-1]
            f = f[:,d-1]
            g = g[:,n-d][::-1]
            h = h[:,n-d][::-1]
        
        return np.concatenate([e,f,g,h])

    def _rotate(self, mat, angle):
        return np.rot90(mat, angle//90, axes = (1,0))

    def __call__(self, face:list=["F", "U", "R", "D", "B", "L"]):
        return [self.sides[self.faces[i]] for i in face]

