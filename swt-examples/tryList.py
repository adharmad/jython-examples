from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *
from org.eclipse.swt.events import *

class TryList:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display, size=(500,500))
        self.shell.setSize(500,500)

        self.list1 = List(self.shell, SWT.MULTI|SWT.H_SCROLL, items=['Strawberry', 'Banana', 'Mango'], bounds=(0,0,60,100))
        self.list1.add('Pickle')

        self.list2 = List(self.shell, SWT.MULTI|SWT.H_SCROLL, items=['Rock', 'Paper', 'Scissors'], mouseDown=self.l2MouseDown, mouseUp=self.l2MouseUp, bounds=(110, 0, 50, 50))

    def l2MouseDown(self, e):
        print self.list2.selection[0] + 'Wins!'

    def l2MouseUp(self, e):
        print 'Try Again'

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryList = TryList()
    tryList.runApp()
