from PyQt5 import QtCore, QtGui, QtWidgets
try:
    from .timer_fnxs import Time_calc
except:
    from timer_fnxs import Time_calc
class Ui_Records(object):
    def __init__(self):
        self.main_window = QtWidgets.QWidget()
        self.main_window.setWindowTitle("Records")
        self.main_window.resize(350,250)
        self.setupUi()
        self.main_window.show()

    def setupUi(self):
        self.records_container = QtWidgets.QHBoxLayout(self.main_window)
        verticalLayout = QtWidgets.QVBoxLayout()
        horizontalLayout = QtWidgets.QHBoxLayout()
        label_mode = QtWidgets.QLabel(self.main_window)
        self.comboBox = QtWidgets.QComboBox(self.main_window)
        self.reload_datas = QtWidgets.QToolButton(self.main_window)
        self.table = QtWidgets.QTableWidget(self.main_window)

        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        label_mode.setText("Select Mode:")

        horizontalLayout.addWidget(label_mode)
        horizontalLayout.addWidget(self.comboBox)
        horizontalLayout.addWidget(self.reload_datas)
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addWidget(self.table)
        self.records_container.addLayout(verticalLayout)
        

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Timer_assest/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload_datas.setIcon(icon)

    def set_table_datas(self, datas):
        mode = self.comboBox.currentText()
        if mode == "":
            self.table.setRowCount(1)
            self.table.setColumnCount(1)
            self.table.setItem(0,0,QtWidgets.QTableWidgetItem("No Records Found"))
        
        else:
            mode_datas = datas["datas"][mode]
            
            column_heads = list(datas["datas"][mode][0][0].keys())
            
            self.table.setRowCount(len(mode_datas))
            self.table.setColumnCount(len(column_heads))
            
            self.table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Date"))
            self.table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Time"))
            self.table.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Comments"))
            
            for row, row_data in enumerate(mode_datas):
                self.table.setVerticalHeaderItem(row, QtWidgets.QTableWidgetItem(str(row+1)))
                
                for column in range(3):
                    val = row_data[0][column_heads[column]]
                    if column == 1:
                        val = Time_calc.parser(None, val)
                        val = val[0:2] + ":" + val[2:4] + ":" + val[4:6]
                    elif column == 0:
                        val = Time_calc.date_parser(None, val)
                    item = QtWidgets.QTableWidgetItem(str(val))
                    self.table.setItem(row, column, item)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
    
    def set_modes(self, datas):
        for mode in list(datas["datas"].keys()):
            self.comboBox.addItem(mode)
