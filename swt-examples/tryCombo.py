from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *
from org.eclipse.swt.events import *

class TryCombo:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display, size=(500,500))
        self.shell.setSize(500,500)

        combo1 = Combo(self.shell, SWT.DROP_DOWN|SWT.READ_ONLY, items=['One', 'Two', 'Three'], location=(0,0), size=(100,200))
        combo1.select(0)

        combo2 = Combo(self.shell, SWT.SIMPLE, items=['Red', 'Green', 'Yellow', 'Blue'], location=(50,50), size=(200,150))
        combo1.select(1)

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryCombo = TryCombo()
    tryCombo.runApp()
