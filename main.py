from PyQt5 import QtCore, QtGui, QtWidgets
from GL import GL_cube
from timer import main

class Ui_MainWindow(object):
    def __init__(self, parent):
        self.main_layout = QtWidgets.QHBoxLayout(Form)
        self.side_pane_layout = QtWidgets.QVBoxLayout()
        
        self.toolButton = QtWidgets.QToolButton(Form)
        
        self.side_pane = QtWidgets.QToolBox(Form)
        self.menu_simulation = QtWidgets.QWidget()
        self.menu_timer = QtWidgets.QWidget()
        self.menu_about = QtWidgets.QWidget()
        
        self.stacked_pages = QtWidgets.QStackedWidget(Form)
        self.page_simulation = QtWidgets.QWidget()
        self.page_timer = QtWidgets.QWidget()
        self.page_about = QtWidgets.QWidget()

        self.gl_cube = GL_cube.cube_main_widget(self.page_simulation ,3)
        self.timer = main.Timer(self.page_timer)
        
        self.setupUi()
        
    def setupUi(self):
        self.side_pane.addItem(self.menu_simulation, "Simulation")
        self.side_pane.addItem(self.menu_timer, "Timer")
        self.side_pane.addItem(self.menu_about, "About")
        
        self.stacked_pages.addWidget(self.page_simulation)
        self.stacked_pages.addWidget(self.page_timer)
        self.stacked_pages.addWidget(self.page_about)
        
        self.side_pane_layout.addWidget(self.toolButton)
        self.side_pane_layout.addWidget(self.side_pane)
        
        self.main_layout.addLayout(self.side_pane_layout)
        self.main_layout.addWidget(self.stacked_pages)

        self.side_pane.currentChanged.connect(self.stacked_pages.setCurrentIndex)
        

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow(Form)    
    
    Form.show()
    app.exec_()