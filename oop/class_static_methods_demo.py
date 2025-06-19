# class_static_methods_demo.py

class Calculator:
    # This is a class attribute
    calculation_type = "Arithmetic Operations"

    # This is a static method — it doesn't use 'self' or 'cls'
    @staticmethod
    def add(a, b):
        return a + b

    # This is a class method — it uses 'cls' to access class data
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
