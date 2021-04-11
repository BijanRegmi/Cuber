try:
    from .Ui import Ui_Timer
    from .timer_fnxs import Time_calc
    from .record_handler import RecordHandler
    from .Records import Ui_Records
except:
    from Ui import Ui_Timer
    from timer_fnxs import Time_calc
    from record_handler import RecordHandler
    from Records import Ui_Records
from time import time_ns, sleep
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QTimer
from math import inf

class Timer(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        
        self.ui = Ui_Timer(parent)
        self._time_measurer = Time_calc()
        self._recorder = RecordHandler()
        self.SetupUI()

        lcd_updater = QTimer(self)
        lcd_updater.setInterval(10)
        lcd_updater.timeout.connect(self.update_lcd)
        lcd_updater.start()
        
    def SetupUI(self):
        self.ui.deck.buttons[0].clicked.connect(self.start_clicked)
        self.ui.deck.buttons[1].clicked.connect(self.pause_clicked)
        self.ui.deck.buttons[2].clicked.connect(self.reset_clicked)
        self.ui.deck.buttons[3].clicked.connect(self.records_clicked)
        self.ui.deck.buttons[4].clicked.connect(self.del_clicked)
        self.ui.deck.buttons[5].clicked.connect(self.dnf_clicked)
        self.ui.deck.buttons[6].clicked.connect(self.ok_clicked)
        self.ui.deck.buttons[7].clicked.connect(self.plus2_clicked)
        
    def start_clicked(self, foo):
        self._time_measurer.start()

    def pause_clicked(self, foo):
        self._time_measurer.pause()

    def reset_clicked(self, foo):
        self._time_measurer.reset()
        self.reset_disp()

    def ok_clicked(self, foo):
        self._recorder.update("3x3", self._time_measurer.elapsed, time_ns())
        self._time_measurer.reset()
        self.reset_disp()

    def del_clicked(self, foo):
        self._time_measurer.reset()
        self.reset_disp()

    def dnf_clicked(self, foo):
        self._recorder.update("3x3", inf, time_ns(), "dnf")
        self._time_measurer.reset()
        self.reset_disp()

    def plus2_clicked(self, foo):
        self._recorder.update("3x3", self._time_measurer.elapsed + 2000000000, time_ns(), comment="+2'ed")
        self._time_measurer.reset()
        self.reset_disp()

    def records_clicked(self, foo):
        rec_win = Ui_Records()
        rec_win.set_modes(self._recorder.datas)
        rec_win.set_table_datas(self._recorder.datas)
        rec_win.reload_datas.clicked.connect(lambda x: rec_win.set_table_datas(self._recorder.datas))
    
    def reset_disp(self):
        for i in range(6):
            self.ui.disp.lcd[i].display(0)
    
    def update_lcd(self):
        if self._time_measurer.state == 1:
            el = self._time_measurer.parser(str(time_ns() - self._time_measurer.initial))
            for i in range(6):
                self.ui.disp.lcd[i].display(int(el[i]))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = QWidget()
    ui = Timer(main_window)
    main_window.show()
    app.exec_()