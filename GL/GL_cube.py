from PyQt5 import QtCore, QtGui, QtWidgets
import OpenGL.GL as gl
import OpenGL.GLU as glu
import numpy as np
from math import dist
try:
    from .cube import Cube
except:
    from cube import Cube

FPS = 60

class cube_main_widget(QtWidgets.QWidget):
    def __init__(self, parent, n):
        super().__init__(parent)
        
        self.horizontalLayout = QtWidgets.QVBoxLayout(parent)
        
        self.glWidget = Cube_GL_Widget(self, n)
        self.horizontalLayout.addWidget(self.glWidget)
        
        self.layer = QtWidgets.QLabel("Activated layer: "+str(self.glWidget.activated_layer))
        self.layer.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addWidget(self.layer)
        
        timer = QtCore.QTimer(self)
        timer.setInterval(1000//FPS)
        timer.timeout.connect(self.glWidget.update)
        timer.start()
        
class Cube_3D(Cube):
    def __init__(self, n):
        self.length = n
        Cube.__init__(self, self.length)

        self.color_rgb_values = {
            "F": (0,     1, 0),
            "B": (0,     0, 1),
            "U": (1,     1, 1),
            "D": (1,     1, 0),
            "R": (1,     0, 0),
            "L": (1, 0.568, 0)
        }
        
        grid_verts_2d = self._create_grid_2d()
        face_verts_2d = self._create_face_2d()

        self.grid_verts_3d = self.create_3d_verts(grid_verts_2d)
        self.face_verts_3d = self.create_3d_verts(face_verts_2d)
    
    def _create_grid_2d(self):
        grid_verts_2d = []
        for i in range(self.length + 1):
            grid_verts_2d.extend([(i, 0), (i, self.length), (0, i) , (self.length, i)])
        
        self.grid_edges = list(range(len(grid_verts_2d)))
        self.grid_color = [0.1,0,0]*(len(grid_verts_2d))
        return grid_verts_2d
        
    def _create_face_2d(self):
        face_verts_2d = []

        for i in range(self.length):
            for j in range(self.length):
                face_verts_2d.extend([(j, i), (j+1, i), (j+1, i+1), (j, i+1)])

        self.face_edges = list(range(len(face_verts_2d)))
        return face_verts_2d
    
    def create_color_pointer(self):
        cube_colors = []
        for face in self.sides:
            face_colors = []
            for row in face[::-1]:
                for elem in row:
                    face_colors.extend([self.color_rgb_values[elem]]*4)
            cube_colors.append(face_colors)
        return cube_colors

    def create_3d_verts(self, verts_2d, normalize=True):
        if normalize:
            n = self.length/2   #normalizer
        else:
            n = 0
        trans_all = []
        for i, j in verts_2d:
            dic = {
                "F":    [i-n, j-n, self.length-n],
                "B":    [self.length-i-n, j-n, 0-n],
                "R":    [self.length-n, j-n, self.length-i-n],
                "L":    [0-n, j-n, i-n],
                "U":    [i-n, self.length-n, self.length-j-n],
                "D":    [i-n, 0-n, j-n]
            }
            trans_all.append(dic)
        
        verts_3d = []
        for x in ["U","D","R","L","F","B"]:
            face = []
            for y in trans_all:
                face.append(y[x])
            verts_3d.append(face)
        return verts_3d
 
class Cube_GL_Widget(QtWidgets.QOpenGLWidget):
    def __init__(self, parent, n = 3):
        QtWidgets.QOpenGLWidget.__init__(self, parent)
        self.parent = parent
        self.manual_rotaion_angle = [0, 0, 0]
        self.auto_rotation_angle = 0
        self.activated_layer = 1
        self.AUTO_ROTATE = False
        self.speed = 20

        self.cube = Cube_3D(n)
        self.set_shortcuts()
    
    def mouseMoveEvent(self, event):
        self.curr_pos = [event.pos().x(), event.pos().y()]
        if self.mouse_btn == 1:
            x = self.curr_pos[0] - self.start_pos[0]
            y = self.curr_pos[1] - self.start_pos[1]
            self.change_manual_rotation_angle(1, x*0.6)
            self.change_manual_rotation_angle(0, y*0.6)
        if self.mouse_btn == 2:
            z = dist(self.start_pos, self.curr_pos)
            if self.start_pos[0] > self.curr_pos[0]: z *= -1
            self.change_manual_rotation_angle(2, z)
        self.start_pos = self.curr_pos
    
    def mousePressEvent(self, event):
        self.mouse_btn = event.button()
        self.start_pos = [event.pos().x(), event.pos().y()]
        
    def set_shortcuts(self):
        view_rots = ["X","Y","Z"]
        moves = ["R","L","F","B","D","U"]
        
        for axis, key in enumerate(view_rots):
            x= QtWidgets.QShortcut(QtGui.QKeySequence(key), self.parent)
            x.activated.connect(lambda a=axis: self.change_manual_rotation_angle(a, 9))

        for rev_axis, key in enumerate(view_rots):
            x= QtWidgets.QShortcut(QtGui.QKeySequence("Shift+"+key), self.parent)
            x.activated.connect(lambda a=rev_axis: self.change_manual_rotation_angle(a, -9))
        
        for move in moves:
            x = QtWidgets.QShortcut(QtGui.QKeySequence(move), self.parent)
            x.activated.connect(lambda m=move: self.cube.move(m, self.activated_layer, 90))        
        
        for rev_move in moves:
            x = QtWidgets.QShortcut(QtGui.QKeySequence("Shift+"+rev_move), self.parent)
            x.activated.connect(lambda m=rev_move: self.cube.move(m, self.activated_layer, -90))

        for layer in range(1, 10):
            x = QtWidgets.QShortcut(QtGui.QKeySequence(str(layer)), self.parent)
            x.activated.connect(lambda l=layer: self.set_layer_selected(l))

        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+R"), self.parent).activated.connect(self.reset_cube)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+V"), self.parent).activated.connect(self.reset_view)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Shift+R"), self.parent).activated.connect(self.hard_reset)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+M"), self.parent).activated.connect(self.set_rotation_mode)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl++"), self.parent).activated.connect(self.cube_increase)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+-"), self.parent).activated.connect(self.cube_decrease)
        QtWidgets.QShortcut(QtGui.QKeySequence("+"), self.parent).activated.connect(self.rpm_increse)
        QtWidgets.QShortcut(QtGui.QKeySequence("-"), self.parent).activated.connect(self.rpm_decrease)

    #Featured Functions
    def cube_increase(self):
        if self.cube.length < 9: self.cube = Cube_3D(self.cube.length + 1)
    def cube_decrease(self):
        if self.cube.length > 1: self.cube = Cube_3D(self.cube.length - 1)
    def reset_cube(self):
        self.cube = Cube_3D(self.cube.length)
        self.activated_layer = 1
    def reset_view(self):
        self.manual_rotaion_angle = [0, 0, 0]
    def hard_reset(self):
        self.reset_cube()
        self.reset_view()
    def set_rotation_mode(self):
        self.AUTO_ROTATE = not self.AUTO_ROTATE
        self.auto_rotation_angle = 0
        self.manual_rotaion_angle = [0,0,0]
    def change_manual_rotation_angle(self, axis, angle):
        self.manual_rotaion_angle[axis] += angle
    def set_layer_selected(self, layer):
        self.activated_layer = layer
        self.parent.layer.setText("Activated layer: "+str(layer))
    def rpm_increse(self):
        self.speed += 1
    def rpm_decrease(self):
        self.speed -= 1
    
    def initializeGL(self):
        gl.glClearColor(0,0,0,0)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glLineWidth(4)
    
    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glPushMatrix()
        gl.glTranslatef(0,0,-3*self.cube.length)
        
        if self.AUTO_ROTATE:
            gl.glRotate(self.auto_rotation_angle, 1,1,1)
            self.auto_rotation_angle += (6*self.speed//FPS)
        else:
            gl.glRotate(self.manual_rotaion_angle[0], 1, 0, 0)
            gl.glRotate(self.manual_rotaion_angle[1], 0, 1, 0)
            gl.glRotate(self.manual_rotaion_angle[2], 0, 0, 1)

        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glEnableClientState(gl.GL_COLOR_ARRAY)
        
        
        for i in self.cube.grid_verts_3d:
            gl.glVertexPointer(3, gl.GL_FLOAT, 0, i)
            gl.glColorPointer(3, gl.GL_FLOAT, 0, self.cube.grid_color)
            gl.glDrawElements(gl.GL_LINES, len(self.cube.grid_edges), gl.GL_UNSIGNED_INT, self.cube.grid_edges)
        
        self.colors = self.cube.create_color_pointer()
        for i,j in enumerate(self.cube.face_verts_3d):
            gl.glVertexPointer(3, gl.GL_FLOAT, 0, j)
            gl.glColorPointer(3, gl.GL_FLOAT, 0, self.colors[i])
            gl.glDrawElements(gl.GL_QUADS, len(self.cube.face_edges), gl.GL_UNSIGNED_INT, self.cube.face_edges)


        gl.glDisableClientState(gl.GL_COLOR_ARRAY)        
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        
        gl.glPopMatrix()

    def resizeGL(self, width, height):
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluPerspective(45, width/height, 1, 100.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = cube_main_widget(None, 3)
    ui.show()
    app.exec_()
