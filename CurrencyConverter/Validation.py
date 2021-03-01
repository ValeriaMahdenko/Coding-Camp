class Validation:
    @staticmethod
    def decorator_string(func):
        def validate_string(self, value):
            if any(map(str.isdigit, value)):
                raise ValueError("No integers in string!")
            return func(self, value)

        return validate_string

    @staticmethod
    def decorator_price(func):
        def validate_price(self, value):
            try:
                x = float(value)
                y = str(x).split('.')
                if len(y[-1]) > 2:
                    raise ValueError("Format of budget is wrong!")
            except ValueError:
                raise ValueError("No letters/characters in number!")
            return func(self, value)

        return validate_price
