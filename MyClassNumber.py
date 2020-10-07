class MyClassNumber:
    def __init__(self, real=0, imag= 0):
        print("its begin class contruction")
        self.real_part=real
        self.imag_part=imag
    def displayComplex(self):
        print("{0}+{1}j".format(self.real_part, self.imag_part))

complx1 = MyClassNumber(10,220)
complx1.displayComplex()

comlex2 = MyClassNumber(20,10)
comlex2.new_attribute=12
comlex2.displayComplex()
print((comlex2.real_part, comlex2.imag_part, comlex2.new_attribute))