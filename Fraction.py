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
        gcd = self.gcd(numerator, denominator)
        self._numerator = numerator // gcd
        self._denominator = denominator // gcd


    def gcd(a, b):
        # calculated using the euclidean algorithm 
        if b == 0:
            return abs(a)
        else:
            Fraction.gcd(b, a % b)


    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass