from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *
from org.eclipse.swt.events import *

class TryButton:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display, size=(500,500))
        self.shell.setSize(500,500)

        button1 = Button(self.shell, SWT.PUSH, text='Hello', location=(0,0), size=(100,20), widgetSelected=self.b1Selected)

        button2 = Button(self.shell,SWT.ARROW,size=(20,20),location=(250,200))
        button3 = Button(self.shell, SWT.FLAT|SWT.TOGGLE, size=(50,50), location=(0,150))
    

    def b1Selected(self, e):
        print 'Button1 was selected'

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryButton = TryButton()
    tryButton.runApp()
