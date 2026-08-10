from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow

def rageCenterHWidget(w):
    box = QHBoxLayout()
    box.addStretch()
    box.addWidget(w)
    box.addStretch()
    return box

def rageCenterVWidget(w):
    box = QVBoxLayout()
    box.addStretch()
    box.addWidget(w)
    box.addStretch()
    return box

def rageCenterHLayout(layout):
    box = QHBoxLayout()
    box.addStretch()
    box.addLayout(layout)
    box.addStretch()
    return box

def rageCenterVLayout(layout):
    box = QVBoxLayout()
    box.addStretch()
    box.addLayout(layout)
    box.addStretch()
    return box

def rageCenterLayout(layout):
    return rageCenterHLayout(rageCenterVLayout(layout))

def rageCenterWidget(widget):
    return rageCenterHLayout(rageCenterVLayout(widget))


class RageCheckBox(QCheckBox):
    def __init__(self, text, index = 0, parent=None):
        super(RageCheckBox, self).__init__(text, parent)
        self.Index = index

    def index(self):
        return self.Index

class RageSpinBox(QSpinBox):
    def __init__(self, index = 0, parent=None):
        super(RageSpinBox, self).__init__(parent)
        self.Index = index

    def index(self):
        return self.Index

class RagePicButton(QAbstractButton):
    def __init__(self, pixmaps, index = 0, parent=None):
        super(RagePicButton, self).__init__(parent)
        self.pixmaps = pixmaps
        self.Index = index
        self.Setting = 0
        self.selected_pixmap = self.pixmaps[self.Setting]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.selected_pixmap)

    def sizeHint(self):
        return self.selected_pixmap.size()
        
    def next(self):
        self.Setting += 1
        if self.Setting >= len(self.pixmaps):
            self.Setting = 0
        self.selected_pixmap = self.pixmaps[self.Setting]
        self.update()
        return self.Setting

    def setting(self):
        return self.Setting

    def setSetting(self, setting):
        self.Setting = setting
        self.selected_pixmap = self.pixmaps[self.Setting]
        self.update()

    def index(self):
        return self.Index

class RageAbsLayout(QLayout):

    def __init__(self, parent=None):
        super(RageAbsLayout, self).__init__(parent)
        self.size = None
        self.items = []

    def add(self, item, rect): # QLayoutItem
        item.setGeometry(rect)
        self.items.append((item, rect))
        if self.size is None:
            self.size = item.widget().sizeHint()

    def addWidget(self, w, pos, sz = None):
        if sz is None:
            sz = w.sizeHint()
        rect = QRect(pos, sz)
        self.add(QWidgetItem(w), rect)

    def addItem(self, item): # QLayoutItem
        self.items.append(item, QRect(0, 0, 0, 0))

    def sizeHint(self):
        if self.size is None:
            return QSize(0, 0)
        return self.size

    def setGeometry(self, rect):
        for a in self.items:
            item = a[0]
            rect = a[1]
            item.setGeometry(rect)

    def itemAt(self, index): # QLayoutItem
        if index >= 0 and index < len(self.items):
            return self.items[index][0]
        return None

    def takeAt(self, index): # QLayoutItem
        if index >= 0 and index < len(self.items):
            return self.items.pop(item)[0]
        return None

    def minimumSize(self):
        return self.size

    def count(self):
        return len(self.items)

def rageMakePicButtons(layout, pts, pixmaps):
    buttons = []
    for i, pt in enumerate(pts):
        button = RagePicButton(pixmaps, i)
        buttons.append(button)
        layout.addWidget(button, pt)
    return buttons

def rageMakeSpinBoxes(layout, pts, max):
    boxes = []
    for i, pt in enumerate(pts):
        box = RageSpinBox(i)
        box.setMaximum(max)
        boxes.append(box)
        layout.addWidget(box, pt)
    return boxes

def TBD(parent):
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Information)
    msg.setText("To Be Done")
    msg.setWindowTitle("TBD")
    return msg.exec_()

