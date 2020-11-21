# -*- coding: utf-8 -*-
"""

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2020-11-03 15:55:15"

import os
import sys
os.environ['QT_PREFERRED_BINDING'] = 'PyQt4;PyQt5;PySide;PySide2'


repo = (lambda f: lambda p=__file__: f(f, p))(
    lambda f, p: p
    if [
        d
        for d in os.listdir(p if os.path.isdir(p) else os.path.dirname(p))
        if d == ".git"
    ]
    else None
    if os.path.dirname(p) == p
    else f(f, os.path.dirname(p))
)()
sys.path.insert(0, repo) if repo not in sys.path else None

from QBinder import Binder, GBinder,FnHook
from Qt import QtGui, QtWidgets, QtCore

import Qt
print(Qt.__binding__)

state = GBinder()
state.msg = "msg"
state.num = "1"
state.input_ui = 1
state.callback = FnHook()

class ButtonTest(QtWidgets.QWidget):
    count = 1
    def __init__(self):
        super(ButtonTest, self).__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        button = QtWidgets.QPushButton("click me")
        layout.addWidget(button)
        label = QtWidgets.QLabel()
        layout.addWidget(label)
        label.setText(lambda: state.num)

        button.clicked.connect(state.callback)
        
    @state("fn_bind")
    def callback(self):
        print("callback",self)
        state.num += '1'
    
class ButtonTest2(QtWidgets.QWidget):
    def __init__(self,widget):
        super(ButtonTest2, self).__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        button = QtWidgets.QPushButton("click me ButtonTest2")
        layout.addWidget(button)

        button.clicked.connect(state.callback) # NOTE auto predict
        # button.clicked.connect(state.callback["input_ui"])
        # button.clicked.connect(state.callback[state.input_ui])
 
        # @state("fn_bind")
        # def callback2(self):
        #     print("callback2",self)
        #     state.num += 3
            
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    # SHOW_INFO_PANEL = True
    # state.input_ui = ButtonTest()
    # state.input_ui.show()
    widget = ButtonTest()
    widget.show()
    widget >> state["input_ui"]
    
    widget2 = ButtonTest2(widget)
    widget2.show()
    sys.exit(app.exec_())