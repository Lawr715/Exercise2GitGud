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
        gcd = 1
        if numerator != 0:
            gcd = self.gcd(numerator, denominator)
        self._numerator = numerator // gcd
        self._denominator = denominator // gcd

    @staticmethod
    def gcd(a, b):
        larger_number = abs(a)
        smaller_number = abs(b)

        if b > a:
            larger_number = abs(b)
            smaller_number = abs(a)
        
        if smaller_number == 0:
            return 0
        for possible_gcd in range(smaller_number, 0, -1):
            if larger_number % possible_gcd == 0 and smaller_number % possible_gcd == 0:
                return possible_gcd

    @property
    def get_numerator(self):
        return str(self._numerator)

    @property
    def get_denominator(self):
        return str(self._denominator)

    def get_fraction(self):
        fraction = self.get_numerator()

        if self._denominator != 1:
            fraction += "/" + self.get_denominator()

        return fraction
