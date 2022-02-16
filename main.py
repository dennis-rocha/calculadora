from re import search
from PyQt5 import QtCore, QtGui, QtWidgets
from core.mainScreen import Ui_MainWindow
from core.io import Calculator


class Calculadora():
    def __init__(self, window) -> None: 
        self.mainWindow = window
        self.Calculator = Calculator()
        self.text = ""
        self.firstNumber = ""
        self.secondNumber = ""
        self.operator = ""
        self.result_message = []
        #self.value = []

        self.mainWindow.btNum_igual.pressed.connect     (lambda: self.outherCliked("="))
        self.mainWindow.btNum_dot.pressed.connect       (lambda: self.outherCliked("."))
        self.mainWindow.btNum_bakspace.pressed.connect  (lambda: self.outherCliked("remove"))
        self.mainWindow.btNum_clear.pressed.connect     (lambda: self.outherCliked("c"))
                
        self.mainWindow.btNum_div.pressed.connect       (lambda: self.operatorClicked("/"))
        self.mainWindow.btNum_multi.pressed.connect     (lambda: self.operatorClicked("*"))
        self.mainWindow.btNum_menos.pressed.connect     (lambda: self.operatorClicked("-"))
        self.mainWindow.btNum_soma.pressed.connect      (lambda: self.operatorClicked("+"))
        self.mainWindow.btNum_pot.pressed.connect       (lambda: self.operatorClicked("^"))

        self.mainWindow.btNum_0.pressed.connect         (lambda: self.numberClicked(0))
        self.mainWindow.btNum_1.pressed.connect         (lambda: self.numberClicked(1))
        self.mainWindow.btNum_2.pressed.connect         (lambda: self.numberClicked(2))
        self.mainWindow.btNum_3.pressed.connect         (lambda: self.numberClicked(3))
        self.mainWindow.btNum_4.pressed.connect         (lambda: self.numberClicked(4))
        self.mainWindow.btNum_5.pressed.connect         (lambda: self.numberClicked(5))
        self.mainWindow.btNum_6.pressed.connect         (lambda: self.numberClicked(6))
        self.mainWindow.btNum_7.pressed.connect         (lambda: self.numberClicked(7))
        self.mainWindow.btNum_8.pressed.connect         (lambda: self.numberClicked(8))
        self.mainWindow.btNum_9.pressed.connect         (lambda: self.numberClicked(9))
        

    def irregularExpression (self,message,value=False):
        self.mainWindow.label.setText((f"{message}") + (f":  {value}" if value else ""))
        self.clear()
        
    def numberClicked(self,n):
        self.text += str(n)
        self.mainWindow.lineEdit.setText(self.text)
        
        
    def operatorClicked(self,operator):
        text = self.getTypeNumber(self.text) 
           
        if text: 
            if not self.firstNumber:
                self.firstNumber = text
                self.text = ""
                
            elif self.operator:
                self.sum_values()
                self.firstNumber = self.getTypeNumber(self.mainWindow.lineEdit.text())
                
        if not self.secondNumber:
            self.operator = operator
            self.mainWindow.lineEdit.setText(f"{operator:^3}")
        
        
            
    def outherCliked(self, operator):
        if operator == "remove":
            self.text = (self.text[:-1]).strip()
            self.mainWindow.lineEdit.setText(self.text if self.text else f"{self.operator:^3}")
            
        elif operator == "c":
            self.clear()
            
        
        elif operator == ".":
            if not search(r"[.]",self.text):
                self.text += "."
        
        else:
            
            if self.firstNumber and self.operator:
                  
                self.secondNumber = self.getTypeNumber(self.text)
                self.sum_values() 
           
      
    def getTypeNumber(self,number):
        if self.text == "":
            return False
        
        else:
            return int(number) if not search(r"[.]", number) else float(number)
        

    
    def sum_values (self):
        validate = self.Calculator.validate_sum([self.firstNumber,self.operator,self.secondNumber])
        
        if validate:
            self.Calculator(validate)
            self.Calculator.calculate()
            self.mainWindow.lineEdit.setText(str(self.Calculator.get_result()))
            self.result_message.append(self.Calculator.menssage)
            if len(self.result_message) > 4:
                self.result_message.pop(0)
            self.mainWindow.label.setText("\n".join(str(i) for i in self.result_message))
            self.clear()
            
            
        else:
            ########## ERRO AQUI
            ######################################
            fill = lambda x: x if x else "N/A"
            text = self.mainWindow.label.text()
            text += "\n" + "Expressão aritmética invalida"
            print(text)
            self.irregularExpression(text, f"{fill(self.firstNumber)} {fill(self.operator)} {fill(self.secondNumber)}")
            
    def clear(self):
        self.text = ""
        self.firstNumber = ""
        self.secondNumber = ""
        self.operator = ""
        self.mainWindow.lineEdit.setText(self.text)
        
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    main_class=Calculadora(ui)
    
    MainWindow.show()
    sys.exit(app.exec_())


