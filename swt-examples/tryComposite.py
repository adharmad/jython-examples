from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *
from org.eclipse.swt.events import *

class TryComposite:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display, size=(500,500))
        self.shell.setSize(500,500)

        color1 = Color(self.display, 0, 0, 0)
        composite1 = Composite(self.shell, SWT.BORDER, bounds=(10,10,270,40), background=Color(self.display, 31,133,31))
        label1 = Label(composite1, SWT.NONE, text='This is a green composite', bounds=(10,10,200,20))

        composite2 = Composite(self.shell, SWT.H_SCROLL|SWT.V_SCROLL, bounds=(30,80,200,200))
        list2 = List(composite2, SWT.MULTI, items=[('Item ' + str(i)) for i in range(50)], size=(300,300))
        

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryComposite = TryComposite()
    tryComposite.runApp()
