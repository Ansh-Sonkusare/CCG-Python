class Car:
    __slots__=["__vin","__make","__model","__year", \
        "__milegae","__fuel"]
    
    def __init__(self, vin,make,model,year):
        self.__vin = vin
        self.__make=make
        self.__model = model
        self.__year = year
        self.__milegae= 0
        self.__fuel=0
    
    def print_car(self):
        print("vin=",self.__vin,", make=",self.__make,", model =", self.__model, \
            "year=",self.__year,self.__milegae,self.__fuel )

def main():
    pass
main()