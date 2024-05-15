class Temperature:
    """
     
    A class to represent temperature values and perform temperature conversions.

    Attributes:
        temp_celsius (float): The temperature value in Celsius.

    Methods:
        __init__: Initializes a Temperature object with a given temperature in Celsius.
        convert_temp_to_fahrenheit: Converts the temperature from Celsius to Fahrenheit.
        convert_fahrenheit_to_cel: Static method to convert temperature from Fahrenheit to Celsius.
        check_valid_temp: Static method to check if a temperature is within valid range.
        create_with_fahrenheit: Class method to create a Temperature object with a given temperature in Fahrenheit.
        standard: Class method to create a Temperature object with a standard value of 0 Celsius.
        __repr__: Returns a string representation of the temperature value.
    
    """
    def __init__(self, temp_celsius):
        self.temp_celsius = temp_celsius

    def convert_temp_to_fahrenheit(self):
        return (self.temp_celsius * 1.8) + 32

    @staticmethod
    def convert_fahrenheit_to_cel(temp_fah):
        return (temp_fah - 32) * 1.8

    @staticmethod
    def check_valid_temp(temp):
        if -273 <= temp <= 3000:
            print("This is a valid temperature")

    @classmethod
    def create_with_fahrenheit(cls, temperature):
        return cls(Temperature.convert_fahrenheit_to_cel(temperature))

    @classmethod
    def standard(cls):
        return cls(0)

    def __repr__(self) -> str:
        temp = str(self.temp_celsius)
        return temp