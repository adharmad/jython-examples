from org.eclipse.swt import *
from org.eclipse.swt.widgets import *
from org.eclipse.swt.graphics import *
from org.eclipse.swt.events import *

class TryTable:
    def __init__(self):
        self.display = Display()
        self.shell = Shell(self.display, size=(500,500))

        table1 = Table(self.shell, SWT.BORDER,
            bounds=(10,10,270,60), linesVisible=1)
        col1 = TableColumn(table1, SWT.LEFT, text='Name', width=50)
        col2 = TableColumn(table1, SWT.RIGHT, text='Age', width=30)
        col3 = TableColumn(table1, SWT.LEFT, text='Addres', width=200)

        item1 = TableItem(table1, SWT.NONE, text=('Amo1', '29', '400 2nd Ave'))
        item2 = TableItem(table1, SWT.NONE, text=('Bags', '26', '902 Niketa-Park'))

        table2 = Table(self.shell, SWT.CHECK|SWT.HIDE_SELECTION,
            bounds=(10,80,270,80), linesVisible=1)
        fruit = TableColumn(table2, SWT.LEFT, text='Fruit', width=100)
        color = TableColumn(table2, SWT.LEFT, text='Color', width=170)

        fruit1 = TableItem(table2, SWT.NONE, text= ('Apple', 'Red'), checked=1)
        fruit2 = TableItem(table2, SWT.NONE, text= ('Mango', 'Blue'), checked=0)

        table3 = Table(self.shell, SWT.FULL_SELECTION, linesVisible=1,
            bounds=(10,180,270,80))
        first = TableColumn(table3, SWT.LEFT, resizable=1,text='First', width=80)
        second = TableColumn(table3, SWT.CENTER, resizable=1,text='Second', width=80)
        third = TableColumn(table3, SWT.RIGHT, resizable=1,text='Third', width=80)

        numbers = ['One', 'Two', 'Three']
        firstItem = TableItem(table3, SWT.NONE, text=numbers)
        secondItem = TableItem(table3, SWT.NONE, text=numbers)
        thirdItem = TableItem(table3, SWT.NONE, text=numbers)
        fourthItem = TableItem(table3, SWT.NONE, text=numbers)
        table3.select(1)

    def runApp(self):
        self.shell.open()
        while not self.shell.isDisposed():
            if not self.display.readAndDispatch():
                self.display.sleep()
        self.display.dispose()

if __name__ == '__main__':    
    tryTable = TryTable()
    tryTable.runApp()
