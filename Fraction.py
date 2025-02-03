class Fraction(object):
    def __init__(self, numerator=0, denominator=1):
        # Handle string input with error handling
        try:
            if isinstance(numerator, str):
                numerator = numerator.strip()  # Remove leading/trailing whitespace
                if '/' in numerator:
                    parts = numerator.split('/')
                    if len(parts) != 2:
                        raise ValueError("Invalid fraction format")
                    num, den = parts
                    numerator, denominator = int(num), int(den)
                else:
                    numerator = int(numerator)

            # Type checking
            if not isinstance(numerator, int) or not isinstance(denominator, int):
                raise TypeError("Both numerator and denominator must be integers")

            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero")

        except (ValueError, TypeError) as e:
            numerator, denominator = 0, 1  # Default to 0/1 on error

        # Handle negative signs
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
            
        # Reduce the fraction using GCD
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            gcd = self.gcd(numerator, denominator)
            self._numerator = numerator // gcd
            self._denominator = denominator // gcd

    @staticmethod
    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        
        a = abs(a)
        b = abs(b)

        while b != 0:
            a, b = b, a % b
        return a

    @property
    def get_numerator(self):
        return str(self._numerator)

    @property
    def get_denominator(self):
        return str(self._denominator)

    def get_fraction(self):
        fraction = str(self._numerator)

        if self._denominator != 1:
            fraction += "/" + str(self._denominator)

        return fraction