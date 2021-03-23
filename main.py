from Ui import Timer
from PyQt5.QtWidgets import QWidget,QApplication
from time import time_ns
from timer_fnxs import Time_calc
from record_handler import RecordHandler
import sys


def start_clicked(foo):
    time_measurer.start()

def pause_clicked(foo):
    time_measurer.pause()

def reset_clicked(foo):
    time_measurer.reset()

def ok_clicked(foo):
    print(time_measurer.elapsed)
    recorder.update("3x3", time_measurer.elapsed)
    time_measurer.reset()

def del_clicked(foo):
    time_measurer.reset()

def dnf_clicked(foo):
    recorder.update("3x3", "dnf")
    time_measurer.reset()

def plus2_clicked(foo):
    recorder.update("3x3", time_measurer.elapsed + 2000000000)
    time_measurer.reset()



app = QApplication(sys.argv)
main_window = QWidget()
ui = Timer(main_window)

time_measurer = Time_calc()
recorder = RecordHandler()

ui.controller.btn_start.clicked.connect(start_clicked)
ui.controller.btn_pause.clicked.connect(pause_clicked)
ui.controller.btn_reset.clicked.connect(reset_clicked)
ui.controller.btn_del.clicked.connect(del_clicked)
ui.controller.btn_dnf.clicked.connect(dnf_clicked)
ui.controller.btn_ok.clicked.connect(ok_clicked)
ui.controller.btn_plus2.clicked.connect(plus2_clicked)

main_window.show()
app.exec_()
recorder.close()