# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# Через функцию
def bonus_for_work(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
    return {name: salary / 100 * bonus for name, salary, bonus in zip(name, salary, (float(i[:-1]) for i in bonus))}


name = ["Name1", "Name2", "Name3", "Name4", "Name5"]
salary = [100, 300, 200, 500, 10]
bonus = ["10.25", "15.10", "7.7", "8.2", "18.9"]

# В одну строку
result = {name: salary / 100 * bonus for name, salary,
          bonus in zip(name, salary, (float(i[:-1]) for i in bonus))}
print(result)

print(bonus_for_work(name, salary, bonus))
