from org.eclipse.swt import *
from org.eclipse.swt.widgets import *

if __name__ == '__main__':
    display = Display()
    shell = Shell(display)

    shell.setSize(100,100)
    shell.open()
    while not shell.isDisposed():
        if not display.readAndDispatch():
            display.sleep()
    display.dispose()
