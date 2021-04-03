from PyQt5 import QtCore, QtGui, QtWidgets

class control_deck():
    def __init__(self, Form):

        #region Creating Layers
        self.control_deck_holder = QtWidgets.QStackedWidget(Form)
        timer_controls = QtWidgets.QWidget()
        layout_timer_controls = QtWidgets.QHBoxLayout()
        self.btn_pause = QtWidgets.QPushButton(timer_controls)
        self.btn_records = QtWidgets.QPushButton(timer_controls)
        self.btn_reset = QtWidgets.QPushButton(timer_controls)
        self.btn_start = QtWidgets.QPushButton(timer_controls)
        time_controls = QtWidgets.QWidget()
        layout_time_controls = QtWidgets.QHBoxLayout()
        self.btn_del = QtWidgets.QPushButton(time_controls)
        self.btn_dnf = QtWidgets.QPushButton(time_controls)
        self.btn_ok = QtWidgets.QPushButton(time_controls)
        self.btn_plus2 = QtWidgets.QPushButton(time_controls)
        #endregion Creating Layers

        #region Creating Layouts
        horizontalLayout_6 = QtWidgets.QHBoxLayout(time_controls)
        horizontalLayout_7 = QtWidgets.QHBoxLayout(timer_controls)
        #endregion Creating Layouts

        #region SetObjectName
        self.control_deck_holder.setObjectName("control_deck_holder")
        timer_controls.setObjectName("timer_controls")
        layout_timer_controls.setObjectName("layout_timer_controls")
        self.btn_pause.setObjectName("btn_pause")
        self.btn_records.setObjectName("btn_records")
        self.btn_reset.setObjectName("btn_reset")
        self.btn_start.setObjectName("btn_start")
        time_controls.setObjectName("time_controls")
        layout_time_controls.setObjectName("layout_time_controls")
        self.btn_del.setObjectName("btn_del")
        self.btn_dnf.setObjectName("btn_dnf")
        self.btn_ok.setObjectName("btn_ok")
        self.btn_plus2.setObjectName("btn_plus2")

        horizontalLayout_7.setObjectName("horizontalLayout_7")
        horizontalLayout_6.setObjectName("horizontalLayout_6")
        #endregion SetObjectName
        
        #region Button Properties
        self.btn_pause.setCheckable(True)
        self.btn_records.setCheckable(True)
        self.btn_reset.setCheckable(True)
        self.btn_start.setCheckable(True)
        self.btn_del.setCheckable(True)
        self.btn_dnf.setCheckable(True)
        self.btn_ok.setCheckable(True)
        self.btn_plus2.setCheckable(True)
        #endregion Button Properties

        #region Setting Icons
        #pause
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Timer_assest/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_pause.setIcon(icon1)
        self.btn_pause.setIconSize(QtCore.QSize(20, 20))

        #records
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Timer_assest/records.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_records.setIcon(icon3)
        self.btn_records.setIconSize(QtCore.QSize(16,16))

        #reset
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Timer_assest/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_reset.setIcon(icon2)
        self.btn_reset.setIconSize(QtCore.QSize(16,16))
        
        #start
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Timer_assest/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_start.setIcon(icon)
        self.btn_start.setIconSize(QtCore.QSize(20, 20))

        #del
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Timer_assest/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_del.setIcon(icon5)
        self.btn_del.setIconSize(QtCore.QSize(20, 20))

        #dnf
        #ok
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Timer_assest/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_ok.setIcon(icon4)
        self.btn_ok.setIconSize(QtCore.QSize(20, 20))

        #plus2
        #endregion Setting Icons
        
        #region Setting Fonts
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dnf.setFont(font)
        self.btn_plus2.setFont(font)
        #endregion Setting Fonts
        
        #region layout properties
        layout_timer_controls.setContentsMargins(10, 10, 10, 10)
        layout_timer_controls.setSpacing(10)
        layout_time_controls.setContentsMargins(10, 10, 10, 10)
        layout_time_controls.setSpacing(10)
        #endregion layout properties
        
        #region Signal and Slot
        self.btn_start.clicked.connect(self._state_running)
        self.btn_pause.clicked.connect(self._state_paused)
        self.btn_reset.clicked.connect(self._state_stopped)
        self.btn_ok.clicked.connect(self._state_stopped)
        self.btn_del.clicked.connect(self._state_stopped)
        self.btn_dnf.clicked.connect(self._state_stopped)
        self.btn_plus2.clicked.connect(self._state_stopped)
        #endregion Signal and Slot
        
        #region ADD WIDGETS
        #timer_controls
        layout_timer_controls.addWidget(self.btn_start)
        layout_timer_controls.addWidget(self.btn_pause)
        layout_timer_controls.addWidget(self.btn_reset)
        layout_timer_controls.addWidget(self.btn_records)
        #time_controls
        layout_time_controls.addWidget(self.btn_ok)
        layout_time_controls.addWidget(self.btn_del)
        layout_time_controls.addWidget(self.btn_dnf)
        layout_time_controls.addWidget(self.btn_plus2)
        #pages inside stacked widget
        self.control_deck_holder.addWidget(timer_controls)
        self.control_deck_holder.addWidget(time_controls)
        #endregion ADD WIDGET
        
        #region ADDING LAYOUTS
        horizontalLayout_6.addLayout(layout_time_controls)
        horizontalLayout_7.addLayout(layout_timer_controls)
        #endregion ADDING LAYOUTS

        self._state_stopped()
        self.setShortcuts(Form)
    
    def setShortcuts(self, Form):
        shortcut_dict = {
            "Space": self._space,
            "Return": self._enter,
            "Del": self._delete,
            "Ctrl + R": self._records,
            "+": self._plus2,
            "Backspace": self._dnf,
            "Esc": self._esc
        }
        for key, fxn in shortcut_dict.items():
            x = QtWidgets.QShortcut(QtGui.QKeySequence(key), Form)
            x.activated.connect(fxn)
    
    def _space(self):
        if self.btn_start.isEnabled():
            self.btn_start.click()
        elif self.btn_pause.isEnabled():
            self.btn_pause.click()
    
    def _enter(self):
        self.btn_ok.click()
        self.btn_reset.click()
    
    def _delete(self):
        self.btn_del.click()
    
    def _records(self):
        self.btn_records.click()

    def _plus2(self):
        self.btn_plus2.click()
    
    def _dnf(self):
        self.btn_dnf.click()
    
    def _esc(self):
        self.btn_reset.click()
        self.btn_del.click()
        QtCore.QCoreApplication.instance().quit()
    
    def _state_stopped(self, sig=None):
        self.btn_start.setEnabled(True)
        self.btn_pause.setEnabled(False)
        self.btn_reset.setEnabled(False)
        self.btn_ok.setEnabled(False)
        self.btn_del.setEnabled(False)
        self.btn_dnf.setEnabled(False)
        self.btn_plus2.setEnabled(False)
        self.control_deck_holder.setCurrentIndex(0)
    
    def _state_running(self, sig=None):
        self.btn_start.setEnabled(False)
        self.btn_pause.setEnabled(True)
        self.btn_reset.setEnabled(True)
        self.btn_ok.setEnabled(False)
        self.btn_del.setEnabled(False)
        self.btn_dnf.setEnabled(False)
        self.btn_plus2.setEnabled(False)
        self.control_deck_holder.setCurrentIndex(0)
    
    def _state_paused(self, sig=None):
        self.btn_start.setEnabled(True)
        self.btn_pause.setEnabled(False)
        self.btn_reset.setEnabled(False)
        self.btn_ok.setEnabled(True)
        self.btn_del.setEnabled(True)
        self.btn_dnf.setEnabled(True)
        self.btn_plus2.setEnabled(True)
        self.control_deck_holder.setCurrentIndex(1)

class display():
    def __init__(self, Form):

        #Form.resize(756, 330)

        #region hierarchy

        #endregion hierarchy
        
        #region Creating Layers
        self.display_holder = QtWidgets.QSplitter(Form)

        layoutWidget = QtWidgets.QWidget(self.display_holder)
        self._colon = QtWidgets.QLabel(self.display_holder)
        layoutWidget_2 = QtWidgets.QWidget(self.display_holder)
        self._colon2 = QtWidgets.QLabel(self.display_holder)
        layoutWidget_3 = QtWidgets.QWidget(self.display_holder)
        
        minutes = QtWidgets.QHBoxLayout(layoutWidget)
        seconds = QtWidgets.QHBoxLayout(layoutWidget_2)
        milliseconds = QtWidgets.QHBoxLayout(layoutWidget_3)
        #endregion Creating Layers

        #region SetObjectName
        Form.setObjectName("Display")

        self.display_holder.setObjectName("display_holder")

        layoutWidget.setObjectName("layoutWidget")
        layoutWidget_2.setObjectName("layoutWidget_2")
        layoutWidget_3.setObjectName("layoutWidget_3")
        
        self._colon.setObjectName("colon")
        self._colon2.setObjectName("dot")

        minutes.setObjectName("minutes")
        seconds.setObjectName("seconds")
        milliseconds.setObjectName("milliseconds")
        #endregion SetObjectName

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
        
        self.display_holder.setOpaqueResize(False)
        self.display_holder.setHandleWidth(0)
        self.display_holder.setChildrenCollapsible(False)
        
        minutes.setSpacing(10)
        seconds.setSpacing(10)
        milliseconds.setSpacing(10)
        #endregion Other Layer Properties
        
class Ui_Timer(control_deck, display):
    def __init__(self, Form):
        Form.setObjectName("Timer")
        Form.resize(420, 80)

        control_deck.__init__(self, Form)
        display.__init__(self, Form)

        #Layout for Main Window
        verticalLayout = QtWidgets.QVBoxLayout(Form)
        verticalLayout.setObjectName("verticalLayout")

        #Main Timer Widget
        timer_holder = QtWidgets.QVBoxLayout()
        timer_holder.setObjectName("timer")

        #Adding Display Holder
        timer_holder.addWidget(self.display_holder)

        #Horizontal Spacer Between Display and Contols
        spacerItem = QtWidgets.QSpacerItem(646, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        timer_holder.addItem(spacerItem)

        #Adding Control Deck Holder
        timer_holder.addWidget(self.control_deck_holder)

        #Vertical Layout to Hold Spacer, Control Deck and Display in Place
        verticalLayout.addLayout(timer_holder)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Timer", "Timer"))

        #region Btn Texts
        self.btn_start.setText(_translate("Form", "Start"))
        self.btn_pause.setText(_translate("Form", "Pause"))
        self.btn_reset.setText(_translate("Form", "Reset"))
        self.btn_records.setText(_translate("Form", "Records"))
        self.btn_ok.setText(_translate("Form", "OK"))
        self.btn_del.setText(_translate("Form", "Del"))
        self.btn_dnf.setText(_translate("Form", "DNF"))
        self.btn_plus2.setText(_translate("Form", "+2"))
        #endregion Btn Texts

        #region Colon text
        self._colon.setText(_translate("Form", """<html><head></head><body ><span style=" font-size:72pt;">:</span></body></html>"""))
        self._colon2.setText(_translate("Form", """<html><head></head><body ><span style=" font-size:72pt;">:</span></body></html>"""))
        #endregion Colon text

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    #Main Window
    main_window = QtWidgets.QWidget()
    
    ui = Ui_Timer(main_window)
    
    main_window.show()
    sys.exit(app.exec_())