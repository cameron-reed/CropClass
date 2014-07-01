from PyQt4.QtGui import *

class ManualGrowDialog(QDialog):
    """this class provides a dialog window to ask for light and water values"""

    #constructor
    def __init__(self):
        super().__init__()

        self.water_spinbox = QSpinBox()
        self.light_spinbox = QSpinBox()

        self.water_spinbox.setRange(0,10)
        self.light_spinbox.setRange(0,10)

        self.water_spinbox.setSuffix(" Water")
        self.light_spinbox.setSuffix(" Light")
