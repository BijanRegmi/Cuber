from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path

class control_deck(QtWidgets.QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)

        #region Creating Pages
        page_timer_controls = QtWidgets.QWidget()
        page_time_controls = QtWidgets.QWidget()
        #endregion Creating Pages
        
        #region Creating Buttons
        self.buttons = []
        for name in ["Start", "Pause", "Reset", "Records", "Del", "DNF", "Ok", "+2"]:
            self.buttons.append(QtWidgets.QPushButton(name))
        #endregion Creating Buttons

        #region Creating Layouts
        layout_timer_controls = QtWidgets.QHBoxLayout()
        layout_time_controls = QtWidgets.QHBoxLayout()
        horizontalLayout1 = QtWidgets.QHBoxLayout(page_time_controls)
        horizontalLayout2 = QtWidgets.QHBoxLayout(page_timer_controls)
        #endregion Creating Layouts
        
        #region Button Properties
        for btn in self.buttons:
            btn.setCheckable(True)
            btn.setFocusPolicy(QtCore.Qt.NoFocus)
        #endregion Button Properties

        #region Setting Icons
        folder_path = str(Path(__file__).parent /'Timer_assest') + "/"
        for idx, name in enumerate(["start.png", "pause.png", "reset.png", "records.png", "delete.png", None, "ok.png", None]):
            if name != None:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(folder_path + name), QtGui.QIcon.Normal, QtGui.QIcon.On)
                self.buttons[idx].setIcon(icon)
                self.buttons[idx].setIconSize(QtCore.QSize(16,16))
        #endregion Setting Icons
        
        #region Setting Fonts
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        for btn in self.buttons:
            btn.setFont(font)
        #endregion Setting Fonts
        
        #region layout properties
        layout_timer_controls.setContentsMargins(10, 10, 10, 10)
        layout_timer_controls.setSpacing(10)
        layout_time_controls.setContentsMargins(10, 10, 10, 10)
        layout_time_controls.setSpacing(10)
        #endregion layout properties
        
        #region Signal and Slot
        self.buttons[0].clicked.connect(self._state_running)
        self.buttons[1].clicked.connect(self._state_paused)
        self.buttons[2].clicked.connect(self._state_stopped)
        self.buttons[6].clicked.connect(self._state_stopped)
        self.buttons[4].clicked.connect(self._state_stopped)
        self.buttons[5].clicked.connect(self._state_stopped)
        self.buttons[7].clicked.connect(self._state_stopped)
        #endregion Signal and Slot
        
        #region ADD WIDGETS
        #timer_controls
        for btn in self.buttons[0:4]:
            layout_timer_controls.addWidget(btn)
        #time_controls
        for btn in self.buttons[4:8]:
            layout_time_controls.addWidget(btn)
        #pages inside stacked widget
        self.addWidget(page_timer_controls)
        self.addWidget(page_time_controls)
        #endregion ADD WIDGET
        
        #region ADDING LAYOUTS
        horizontalLayout1.addLayout(layout_time_controls)
        horizontalLayout2.addLayout(layout_timer_controls)
        #endregion ADDING LAYOUTS

        self._state_stopped()
        self.setShortcuts(parent)
    
    def setShortcuts(self, parent):
        shortcut_dict = {
            "Space": self._space,
            "Return": self._enter,
            "Del": self._delete,
            "R": self._records,
            "+": self._plus2,
            "Backspace": self._dnf,
            "Esc": self._esc
        }
        for key, fxn in shortcut_dict.items():
            x = QtWidgets.QShortcut(QtGui.QKeySequence(key), parent)
            x.activated.connect(fxn)
    
    def _space(self):
        if self.buttons[0].isEnabled(): self.buttons[0].click()
        elif self.buttons[1].isEnabled(): self.buttons[1].click()
    
    def _enter(self):
        self.buttons[6].click()
        self.buttons[2].click()
    
    def _delete(self):
        self.buttons[4].click()
    
    def _records(self):
        self.buttons[3].click()

    def _plus2(self):
        self.buttons[7].click()
    
    def _dnf(self):
        self.buttons[5].click()
    
    def _esc(self):
        self.buttons[2].click()
        self.buttons[4].click()
        QtCore.QCoreApplication.instance().quit()
    
    def _state_stopped(self, sig=None):
        for idx, btn in enumerate(self.buttons):
            if idx in [0, 3]:
                btn.setEnabled(True)
            else:
                btn.setEnabled(False)
        self.setCurrentIndex(0)
    
    def _state_running(self, sig=None):
        for idx, btn in enumerate(self.buttons):
            if idx in [1, 2]:
                btn.setEnabled(True)
            else:
                btn.setEnabled(False)
        self.setCurrentIndex(0)
    
    def _state_paused(self, sig=None):
        for idx, btn in enumerate(self.buttons):
            if idx in [1, 2]:
                btn.setEnabled(False)
            else:
                btn.setEnabled(True)
        self.setCurrentIndex(1)

class display(QtWidgets.QSplitter):
    def __init__(self, parent):
        super().__init__(parent)
        
        #region Creating Widgets
        layoutWidget = QtWidgets.QWidget(self)
        self._colon = QtWidgets.QLabel(self)
        layoutWidget_2 = QtWidgets.QWidget(self)
        self._colon2 = QtWidgets.QLabel(self)
        layoutWidget_3 = QtWidgets.QWidget(self)
        
        minutes = QtWidgets.QHBoxLayout(layoutWidget)
        seconds = QtWidgets.QHBoxLayout(layoutWidget_2)
        milliseconds = QtWidgets.QHBoxLayout(layoutWidget_3)
        #endregion Creating Widgets

        #region Create LCDS
        self.lcd = []
        for i in range(6):
            self.lcd.append(QtWidgets.QLCDNumber(layoutWidget))
            self.lcd[i].setFrameShape(QtWidgets.QFrame.NoFrame)
            self.lcd[i].setDigitCount(1)
            self.lcd[i].setObjectName("lcd_" + str(i))
        #endregion Create LCDS
        
        #region ADD LCDS
        minutes.addWidget(self.lcd[0])
        minutes.addWidget(self.lcd[1])
        seconds.addWidget(self.lcd[2])
        seconds.addWidget(self.lcd[3])
        milliseconds.addWidget(self.lcd[4])
        milliseconds.addWidget(self.lcd[5])
        #endregion ADD LCDS

        #region Other Layer Properties
        self._colon.setScaledContents(True)
        self._colon.setAlignment(QtCore.Qt.AlignCenter)
        self._colon.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        
        self._colon2.setScaledContents(True)
        self._colon2.setAlignment(QtCore.Qt.AlignCenter)
        self._colon2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        
        self.setOpaqueResize(False)
        self.setHandleWidth(0)
        self.setChildrenCollapsible(False)
        
        minutes.setSpacing(10)
        seconds.setSpacing(10)
        milliseconds.setSpacing(10)
        #endregion Other Layer Properties

        self.retranslateUi(parent)
    
    def retranslateUi(self, parent):
        _translate = QtCore.QCoreApplication.translate
        
        #region Colon text
        self._colon.setText(_translate("parent", """<html><head></head><body ><span style=" font-size:72pt;">:</span></body></html>"""))
        self._colon2.setText(_translate("parent", """<html><head></head><body ><span style=" font-size:72pt;">:</span></body></html>"""))
        #endregion Colon text
        
class Ui_Timer(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        
        self.disp = display(parent)
        spacer = QtWidgets.QSpacerItem(646, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.deck = control_deck(parent)

        #Layout for Main Window
        verticalLayout = QtWidgets.QVBoxLayout(parent)
        
        #Main Timer Widget
        timer_holder = QtWidgets.QVBoxLayout()
        
        #Adding Widgets
        timer_holder.addWidget(self.disp)
        timer_holder.addItem(spacer)
        timer_holder.addWidget(self.deck)

        #Vertical Layout to Hold Spacer, Control Deck and Display in Place
        verticalLayout.addLayout(timer_holder)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    #Main Window
    main_window = QtWidgets.QWidget()
    
    ui = Ui_Timer(main_window)
    
    main_window.show()
    sys.exit(app.exec_())