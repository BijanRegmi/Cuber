from PyQt5 import QtCore, QtGui, QtWidgets

class Cubie(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        QtWidgets.QComboBox.__init__(self, parent)
        
        self.model = QtGui.QStandardItemModel(0, 0)
        self.colors = ['red', 'orange', 'green', 'blue', 'yellow', 'white' ]
        
        for color in self.colors:
            item = QtGui.QStandardItem()
            item.setBackground(QtGui.QColor(color))
            self.model.appendRow(item)
       
        self.setModel(self.model)
        self.activated['int'].connect(self.changedIndex)

    def changedIndex(self, value):
        self.setStyleSheet("QWidget {background-color: %s}" % self.colors[value])

class Face(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.columnLayout = QtWidgets.QVBoxLayout(self)
        rowLayouts = [QtWidgets.QHBoxLayout(),QtWidgets.QHBoxLayout(),QtWidgets.QHBoxLayout()]


        self.cubies = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(Cubie())
            self.cubies.append(temp)
        
        for i, row in enumerate(self.cubies):
            for cubie in row:
                rowLayouts[i].addWidget(cubie)
            self.columnLayout.addLayout(rowLayouts[i])

class ManualInput(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.faces = []
        
        for i in range(6):
            self.faces.append(Face())
        
        self.gridLayout.addWidget(self.faces[0], 0, 1, 1, 1)
        self.gridLayout.addWidget(self.faces[1], 1, 0, 1, 1)
        self.gridLayout.addWidget(self.faces[2], 1, 1, 1, 1)
        self.gridLayout.addWidget(self.faces[3], 1, 2, 1, 1)
        self.gridLayout.addWidget(self.faces[4], 1, 3, 1, 1)
        self.gridLayout.addWidget(self.faces[5], 2, 1, 1, 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = ManualInput()
    Form.show()
    sys.exit(app.exec_())
