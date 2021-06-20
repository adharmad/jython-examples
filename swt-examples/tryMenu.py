from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *
from org.eclipse.swt.events import *

class TryMenu:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display, size=(500,500))

        menu = Menu(self.shell, SWT.BAR)
        self.shell.setMenuBar(menu)
        file = MenuItem(menu, SWT.CASCADE, text='File')
        
        fileMenu = Menu(self.shell, SWT.DROP_DOWN)
        file.setMenu(fileMenu)
        fileItem1 = MenuItem(fileMenu, SWT.PUSH, text='New')
        fileItem2 = MenuItem(fileMenu, SWT.PUSH, text='Close')
        fileItem3 = MenuItem(fileMenu, SWT.PUSH, text='Open')
        #fileItem1.addListener(SWT.Selection, Listener(handleEvent=self.fileItem1Listener))

    def fileItem1Listener(self, e):
        print 'New file selected'
        
        
        

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryMenu = TryMenu()
    tryMenu.runApp()
