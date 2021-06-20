from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *

class TryLabel:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display)
        self.shell.setSize(500,500)

        label1 = Label(self.shell, SWT.BORDER)
        label1.setText('See no evil')
        label1.setSize(100, 20)
        label1.setLocation(30, 30)

        sep1 = Label(self.shell, SWT.SEPARATOR|SWT.HORIZONTAL|SWT.SHADOW_IN)
        sep1.setBounds(30, 60, 100, 20)

        label2 = Label(self.shell, SWT.NONE)
        label2.setText('Hear No Evil')
        label2.setSize(100, 20)
        label2.setLocation(30, 90)

        sep2 = Label(self.shell, SWT.SEPARATOR|SWT.HORIZONTAL)
        sep2.setBounds(30, 120, 100, 20)

        label3 = Label(self.shell, SWT.NONE)
        label3.setText('Speak No Evil')
        label3.setSize(100, 20)
        label3.setLocation(30, 150)
        label3.setBackground(Color(self.display, 200, 111, 50))

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryLabel = TryLabel()
    tryLabel.runApp()
