class Calculator:
    def __init__(self,value=None) -> None:
        self.value = value
        self.res = 0
        self.menssage = ""
        self.operadores = {
            "+":lambda x,y : x+y,
            "-":lambda x,y : x-y,
            "*":lambda x,y : x*y,
            "^":lambda x,y : x**y,
            "/":lambda x,y : x/y,
            "%":lambda x,y : x%y
        }
             
             
    def __call__(self, value):
        self.value=value
        
    def __str__(self) -> str:
        return self.menssage
    
    def calculate(self):
        num1 = self.value[0]
        op = self.value[1]
        num2 = self.value[2]
        self.res = self.operadores[op](num1,num2)
        self.menssage = f"{self.value[0]} {self.value[1]} {self.value[2]} = {self.res}"
    
    def get_result(self) -> None:
        return self.res
    
    
    def validate_sum(self,value):
        if len(value) < 3:
            return False
        
        type_value = lambda x,y: x == y
        fill1 = type_value(type(value[0]), int) or type_value(type(value[0]), float)
        fill2 = type_value(type(value[2]), int) or type_value(type(value[2]), float)
        
        if not type_value(fill1,fill2):
            return False
        
        if value[1] not in ["+","-","*","^","/"]:
            return False
        
        return value

        