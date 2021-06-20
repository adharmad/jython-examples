from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *
from org.eclipse.swt.events import *

class TryTab:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display, size=(500,500))

        tab1 = TabFolder(self.shell, SWT.NONE, bounds=(10,10,270,250))
        buttonComp = Composite(tab1, SWT.NONE)
        button1 = Button(buttonComp, SWT.PUSH, location=(0,0), size=(100,100),text='Hello')
        button2 = Button(buttonComp, SWT.ARROW, location=(150,0), size=(50,50))
        item1 = TabItem(tab1, SWT.NONE, text='Buttons', control=buttonComp)

        labelComp = Composite(tab1, SWT.NONE)
        lab1 = Label(labelComp, SWT.NONE, text='Here are some labels',
            bounds=(0,0,250,20))
        lab2 = Label(labelComp, SWT.NONE, text='Some more labels',
            bounds=(0,40,200,20))
        item2 = TabItem(tab1, SWT.NONE, text='Labels', control=labelComp)
        

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryTab = TryTab()
    tryTab.runApp()
