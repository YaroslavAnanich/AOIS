class IEEE754Number:
    sign = 0
    binary_exponent = None
    exponent = None
    mantissa = None

    def __init__(self, binary_exponent, exponent, mantissa):
        self.binary_exponent = binary_exponent
        self.exponent = exponent
        self.mantissa = mantissa

    def print_info(self):
        print(f'IEEE 574 {self.sign}|{self.binary_exponent}|{self.mantissa}')
