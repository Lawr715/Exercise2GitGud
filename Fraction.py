class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        # Handle string input
        if isinstance(numerator, str):
            numerator = numerator.strip()  # Remove leading/trailing whitespace
            if '/' in numerator:
                num, den = numerator.split('/')
                numerator = int(num)
                denominator = int(den)

        # Type checking
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Both numerator and denominator must be integers")

        if denominator == 0:
            raise ZeroDivisionError
            
        # Handle negative signs
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
            
        # Reduce the fraction using GCD
        gcd = self.gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass

class ZeroDivisionError(Exception):
    def __init__(self, message="Denominator cannot be zero"):
        self.message = message
        super.__init__(self.message)