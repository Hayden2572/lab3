from decimal import Decimal, getcontext
from fractions import Fraction
from datetime import datetime, date

listComprehension = [x**2 for x in range(1, 11)]
listComprehensionSort = [x for x in range(1, 21) if x % 2 == 0]
ogList = ["python", "Java", "c++", "Rust", "go"]
sortedList = [word for word in ogList if len(word) > 3 and word.istitle()]

class Countdown:
    def __init__(self, n):
        self.current = n
        self.end = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

for x in Countdown(5):
    print(x)

def Phibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, b+a
        print(a, b)

for x in Phibonacci(5):
    print(x)

getcontext().prec = 10

def deposit_calculator():
    initial_amount = Decimal(input("Введите начальную сумму вклада (рубли.копейки): "))
    annual_rate = Decimal(input("Введите годовую процентную ставку (например, 7.5): "))
    years = int(input("Введите срок вклада (в годах): "))

    months = years * 12
    monthly_rate = annual_rate / (12 * 100)
    total_amount = initial_amount * (1 + monthly_rate) ** months

    total_amount = total_amount.quantize(Decimal('0.01'))

    profit = total_amount - initial_amount

    print(f"Итоговая сумма вклада: {total_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")

deposit_calculator()

frac1 = Fraction(3, 4)
frac2 = Fraction(5, 6)

addition = frac1 + frac2
subtraction = frac1 - frac2
multiplication = frac1 * frac2
division = frac1 / frac2

print(f"Сложение: {addition}")
print(f"Вычитание: {subtraction}")
print(f"Умножение: {multiplication}")
print(f"Деление: {division}")

now = datetime.now()

print(f"Текущая дата и время: {now}")
print(f"Только текущая дата: {now.date()}")
print(f"Только текущее время: {now.time()}")

birthday_str = input("Введите вашу дату рождения (гггг-мм-дд): ")
birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()

today = date.today()

days_passed = (today - birthday).days
print(f"С момента рождения прошло дней: {days_passed}")

next_birthday = birthday.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_until_next_birthday = (next_birthday - today).days
print(f"До следующего дня рождения осталось дней: {days_until_next_birthday}")

def format_datetime(dt):
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    return f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {dt.strftime('%H:%M')}"

now = datetime.now()
print(format_datetime(now))