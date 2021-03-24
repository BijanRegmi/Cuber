from Ui import Ui_Timer
from PyQt5.QtWidgets import QWidget,QApplication
from time import time_ns, sleep
from timer_fnxs import Time_calc
from record_handler import RecordHandler
import sys
from threading import Thread

class Timer():
    def __init__(self, Form):
        self.timer_thread = Thread(target=self.update_lcd)
        self.app_running = True
        self.ui = Ui_Timer(Form)
        self._time_measurer = Time_calc()
        self._recorder = RecordHandler()
        self.SetupUI()
        
    def SetupUI(self):
        self.timer_thread.start()
        self.ui.controller.btn_start.clicked.connect(self.start_clicked)
        self.ui.controller.btn_pause.clicked.connect(self.pause_clicked)
        self.ui.controller.btn_reset.clicked.connect(self.reset_clicked)
        self.ui.controller.btn_del.clicked.connect(self.del_clicked)
        self.ui.controller.btn_dnf.clicked.connect(self.dnf_clicked)
        self.ui.controller.btn_ok.clicked.connect(self.ok_clicked)
        self.ui.controller.btn_plus2.clicked.connect(self.plus2_clicked)


    def start_clicked(self, foo):
        self._time_measurer.start()

    def pause_clicked(self, foo):
        self._time_measurer.pause()

    def reset_clicked(self, foo):
        self._time_measurer.reset()
        self.reset_disp()

    def ok_clicked(self, foo):
        self._recorder.update("3x3", self._time_measurer.elapsed)
        self._time_measurer.reset()
        self.reset_disp()

    def del_clicked(self, foo):
        self._time_measurer.reset()
        self.reset_disp()

    def dnf_clicked(self, foo):
        self._recorder.update("3x3", "dnf")
        self._time_measurer.reset()
        self.reset_disp()

    def plus2_clicked(self, foo):
        self._recorder.update("3x3", self._time_measurer.elapsed + 2000000000, comment="+2'ed")
        self._time_measurer.reset()
        self.reset_disp()

    def reset_disp(self):
        for i in range(6):
            self.ui.lcd.lcd[i].display(0)

    def update_lcd(self):
        while self.app_running:
            while self._time_measurer.state == 1:
                el = self._time_measurer.parser(str(time_ns() - self._time_measurer.initial))
                for i in range(6):
                    self.ui.lcd.lcd[i].display(int(el[i]))
                sleep(0.01)
                


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QWidget()
    ui = Timer(main_window)
    main_window.show()
    app.exec_()
    ui._recorder.close()
    ui.app_running = False