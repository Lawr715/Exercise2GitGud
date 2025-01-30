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
        pass

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