class Employee:
    def __init__(self, name, salary):
        self._name = name           # Protected attribute
        self.__salary = salary      # Private attribute

    def display(self):
        print(f"Name: {self._name}")
        print(f"Salary: {self.__salary}")

    def _calculate_bonus(self):
        return self.__salary * 0.1   # Protected method

    def __increase_salary(self, amount):
        self.__salary += amount      # Private method

    def give_bonus(self):
        bonus = self._calculate_bonus()
        self.__increase_salary(bonus)
        print(f"Bonus of {bonus} added. New salary: {self.__salary}")

# Create an instance of the Employee class
employee = Employee("John Doe", 5000)

# Accessing protected attribute (convention, not enforced)
print(employee._name)         # Output: John Doe

# Accessing private attribute (name mangling)
print(employee._Employee__salary)   # Output: 5000

# Accessing attributes using the display method
employee.display()            # Output: Name: John Doe, Salary: 5000

# Accessing protected method
bonus = employee._calculate_bonus()
print(bonus)                  # Output: 500

# Trying to access private method (name mangling)
employee._Employee__increase_salary(1000)  # Raises AttributeError

# Accessing private method indirectly
employee.give_bonus()         # Output: Bonus of 500 added. New salary: 5500
employee.display()            # Output: Name: John Doe, Salary: 5500
