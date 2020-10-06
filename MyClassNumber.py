class MyClassNumber:
    def __init__(self, real=0, imag= 0):
        print("its begin class contruction")
        self.real_part=real
        self.imag_part=imag
    def displayComplex(self):
        print("{0}+{1}j".format(self.real_part, self.imag_part))

complx1 = MyClassNumber(10,220)
complx1.displayComplex()