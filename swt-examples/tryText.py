from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *

class TryText:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display)
        self.shell.setSize(500,500)

        text1 = Text(self.shell, SWT.BORDER)
        text1.setTextLimit(30)
        text1.setText('Type something here')
        text1.setBounds(10, 10, 200, 20)

        text2 = Text(self.shell, SWT.NONE)
        text2.setEchoChar('*')
        text2.setBounds(10, 50, 200, 20)
        text2.setText('Password')

        text3 = Text(self.shell, SWT.BORDER|SWT.H_SCROLL|SWT.V_SCROLL, bounds=(10,90,200,20), editable=0, text='Bet you cannot type here')
        #text3.bounds = (10, 90, 200, 20)

        

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryText = TryText()
    tryText.runApp()
