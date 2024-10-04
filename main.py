import random
from colorama import Fore, Style

class Encryptor:
    def __init__(self, numbers):
        self._number = numbers
        self._result = self._perform_random_operation()

    def _perform_random_operation(self):
        operations = [
            lambda x: x + random.randint(1, 10),  # Додавання
            lambda x: x - random.randint(1, 10),  # Віднімання
            lambda x: x * random.randint(1, 5),   # Множення
            lambda x: x / random.randint(1, 5)     # Ділення
        ]
        operation = random.choice(operations)
        return operation(self._number)

    def __str__(self):
        return f"{Fore.GREEN}Результат обчислень: {Style.BRIGHT}{self._result}{Style.RESET_ALL}"

if __name__ == "__main__":
    number = int(input("Введіть число для шифрування: "))
    encryptor = Encryptor(number)
    print(encryptor)
