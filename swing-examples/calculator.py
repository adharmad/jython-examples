import javax.swing as swing
import java.awt as awt
import java
import operator

class CalculatorFrame(swing.JFrame):
   
    operators = { '/' : operator.div, '*' : operator.mul, 
        '-' : operator.sub, '+' : operator.add }
    
    operatorString = '/*+='
    
    def __init__(self):
        swing.JFrame.__init__(self, title='Calculator', size=(200,250))
        self.keyReleased = self.key
        self.contentPane.layout = awt.BorderLayout()
        self.contentPane.add(self.buildDisplayPanel(),
            awt.BorderLayout.NORTH) 
        self.contentPane.add(self.buildDigitPanel(),
            awt.BorderLayout.WEST) 
        self.contentPane.add(self.buildOperatorPanel(),
            awt.BorderLayout.EAST)

    def buildDisplayPanel(self):
        panel = swing.JPanel(size=(200,100),
            border=swing.border.TitledBorder('Display'),
            layout=awt.BorderLayout(0,10))
        self.topOperand = swing.JTextField(preferredSize=(200,20),
            editable=0, background=(255,255,255),
            horizontalAlignment=swing.SwingConstants.RIGHT)
        panel.add(self.topOperand, awt.BorderLayout.NORTH)
        self.operator = swing.JTextField(preferredSize=(160,20),
            editable=0, background=(255,255,255))
        panel.add(self.operator, awt.BorderLayout.WEST)
        self.bottomOperand = swing.JTextField(preferredSize=(160,20),
            editable=0, background=(255,255,255),
            horizontalAlignment=swing.SwingConstants.RIGHT)
        panel.add(self.bottomOperand, awt.BorderLayout.EAST)
        return panel

    def buildDigitPanel(self):
        box = swing.Box.createVerticalBox()
        box.add(self.buildDigitRow((7, 8, 9)))
        box.add(self.buildDigitRow((4, 5, 6)))
        box.add(self.buildDigitRow((1, 2, 3)))
        box.add(self.buildDigitRow((0,)))
        box.add(self.buildFunctionRow())
        return box
    
    def buildDigitRow(self, digits):
        row = swing.Box.createHorizontalBox()
        for eachDigit in digits:
            if eachDigit:
                button = swing.JButton(str(eachDigit), 
                    actionPerformed=self.digitPressed)
                row.add(button)
        return row

    def buildFunctionRow(self):
        row = swing.Box.createHorizontalBox()
        row.add(swing.JButton('Clr', actionPerformed=self.clear))
        row.add(swing.JButton('.', actionPerformed=self.decimalPressed))
        return row

    def buildOperatorPanel(self):
        box = swing.Box.createHorizontalBox()
        for operator in self.operatorString:
            box.add(swing.JButton(operator,
                actionPerformed=self.operatorPressed))
        return box
    
    def digitPressed(self, event):
        self.handleDigit(event.source.text)

    def operatorPressed(self, event): 
        self.handleOperator(event.source.text)

    def key(self, event):
        char = event.keyChar
        if char.isDigit():
            self.handleDigit(char)
        elif char == '.':
            self.decimalPressed(event)
        elif char in self.operatorString:
            self.handleOperator(char)
        elif char == '\n':
            self.clear(event)

    def clear(self, event):
        self.operator.text = ''
        self.topOperand.text = ''
        self.bottomOperand.text = ''

    def handleDigit(self, digitChar):
        self.bottomOperand.text += digitChar

    def decimalPressed(self, event):
        if not '.' in self.bottomOperand.text:
            self.bottomOperand.text += '.'

    def handleOperator(self, opChar):
        if self.operator.text:
            opFunc = self.operators[self.operator.text]
            topNum = float(self.topOperand.text)
            bottomNum = float(self.bottomOperand.text)
            result = opFunc(topNum, bottomNum)
            self.topOperand.text = str(result)
            self.bottomOperand.text = ''
        elif self.bottomOperand.text:
            self.topOperand.text = self.bottomOperand.text
            self.bottomOperand.text = ''
        self.displayOperator(opChar)

    def displayOperator(self, opChar):
        if not self.calculationStarted():
            return
        if opChar == '=':
            self.operator.text = ''
        else:
            self.operator.text = opChar

    def calculationStarted(self):
        return self.topOperand.text or self.bottomOperand.text

if __name__ == '__main__':
    CalculatorFrame().show()
