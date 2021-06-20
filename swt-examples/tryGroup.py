from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *
from org.eclipse.swt.events import *

class TryGroup:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display, size=(500,500))

        group1 = Group(self.shell, SWT.BORDER, bounds=(30,30,200,200),
            text='Group 1')
        button1 = Button(group1, SWT.PUSH, bounds=(10,20,80,20),
            text='I am in a group')
        label1 = Label(group1, SWT.NONE, bounds=(10,50,80,20),
            text='So am I!!')
        
        group2 = Group(group1, SWT.BORDER, bounds=(10,100,150,50),
            text='A group inside Group1',
            background=Color(self.display, 233,20,233))
        button2 = Button(group2, SWT.PUSH, bounds=(10,20,50,20),
            text='Twice........')

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryGroup = TryGroup()
    tryGroup.runApp()
