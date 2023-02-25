from auth import register
from operation import add, sub, mn, dil, cos, sin, tg
import json
import datetime

def wr(data, n):
    with open(n, 'a+') as file:
        json.dump(data, file, indent=3)

def view_history():
    with open('history.json') as file:
        data = json.load(file)
        for entry in data:
            print(
                f'Time: {entry["time"]}, Operation: {entry["operation"]}, Operands: {entry["operands"]}, Result: {entry["result"]}')


while True:
    time = datetime.datetime.now()
    c = str(input("Введите операцию (+, -, *, /, cos, sin, tg) или H для просмотра истории или S для выхода: "))
    if c == "S":
        break
    if c == "H":
        view_history()
        continue
    if c in ("+", "-", "*", "/", "cos", "sin", "tg"):
        a = float(input("Введите первое число: "))
        b = None
        if c in ("+", "-", "*", "/"):
            b = float(input("Введите второе число: "))

        if c == "+":
            result = add(a, b)
            print(f'{a} + {b} = {result}')
        elif c == "-":
            result = sub(a, b)
            print(f'{a} - {b} = {result}')
        elif c == "*":
            result = mn(a, b)
            print(f'{a} * {b} = {result}')
        elif c == "/":
            if b != 0:
                result = dil(a, b)
                print(f'{a} / {b} = {result}')
            else:
                raise ZeroDivisionError("ZeroDivision")
        elif c == "cos":
            result = cos(a)
            print(f'cos({a}) = {result}')
        elif c == "sin":
            result = sin(a)
            print(f'sin({a}) = {result}')
        elif c == "tg":
            result = tg(a)
            print(f'tg({a}) = {result}')
        else:
            raise ValueError("Error: unsupported operation")

        n_data = {
            "time": str(time),
            "operation": c,
            "operands": [a, b] if b else [a],
            "result": result
        }
        history = []
        history.append(n_data)
        wr(history, 'history.json')

    else:
        raise ValueError("Error: unsupported operation")





















