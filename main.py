import json
import os

class Car():
    def __init__(self, name=0, model=0, color=0, L=0, price=0, D_LF=0, D_RF=0, D_LB=0, D_RB=0, fara_l=0, fara_r=0):
        self.name = name
        self.model = model
        self.color = color
        self.L = L
        self.price = price
        self.D_LF = D_LF
        self.D_RF = D_RF
        self.D_LB = D_LB
        self.D_RB = D_RB
        self.fara_l = fara_l
        self.fara_r = fara_r
        if name != 0:
            self.save()

    def info(self):
        return f"""Марка: {self.name}
Модель: {self.model}
Цвет: {self.color}
Литраж двигателя: {self.L} 
Стоимость: {self.price}
Состояние дверей:
    Левая передняя дверь: {self.D_LF}
    Правая передняя дверь: {self.D_RF}
    Левая задняя дверь: {self.D_LB}
    Правая задняя дверь: {self.D_RB}
Состояние фар:
    Левая: {self.fara_l}
    Правая: {self.fara_r}"""

    def save(self):
        with open(f"data/cars/{self.name}.json", "w", encoding="utf-8") as w_file:
            car = {
                "name": self.name,
                "model": self.model,
                "color": self.color,
                "L": self.L,
                "price": self.price,
                "D_LF": self.D_LF,
                "D_RF": self.D_RF,
                "D_LB": self.D_LB,
                "D_RB": self.D_RB,
                "fara_l": self.fara_l,
                "fara_r": self.fara_r
            }
            json.dump(car, w_file)
        with open("data/names.json", "r", encoding="utf-8") as r_file:
            names = json.load(r_file)
            if self.name not in names["names"]:
                names["names"].append(self.name)
                with open(f"data/names.json", "w", encoding="utf-8") as r_file:
                    json.dump(names, r_file)
        if self.name not in car_dict:
            car_dict[self.name] = car

    def restore(self, name):
        with open(f"data/cars/{name}.json", "r") as r_file:
            car = json.load(r_file)
            self.name = car["name"]
            self.model = car["model"]
            self.color = car["color"]
            self.L = car["L"]
            self.price = car["price"]
            self.D_LF = car["D_LF"]
            self.D_RF = car["D_RF"]
            self.D_LB = car["D_LB"]
            self.D_RB = car["D_RB"]
            self.fara_l = car["fara_l"]
            self.fara_r = car["fara_r"]
            self.save()

    def DEL(self):
        os.remove(f"data/cars/{self.name}.json")
        if self.name in car_dict.keys():
            del car_dict[self.name]
        with open("data/names.json", "r", encoding="utf-8") as r_file:
            names = json.load(r_file)
            if self.name in names["names"]:
                names["names"].remove(self.name)
                with open(f"data/names.json", "w", encoding="utf-8") as r_file:
                    json.dump(names, r_file)
        self = None

    def PROV_na_dobavlenie(self):
        with open("data/names.json", "r", encoding="utf-8") as r_file:
            names = json.load(r_file)["names"]
            if self.name in names["names"]:
                return "Машина успешно добавлена."
            else:
                return "Ошибка."

def output():
    with open("data/names.json", "r", encoding="utf-8") as r_file:
        names = json.load(r_file)["names"]
    out = ""
    for num, elem in enumerate(names):
        out += f"{num + 1}) {elem}\n"
    return out

def insex_to_name(index):
    with open("data/names.json", "r", encoding="utf-8") as r_file:
        names = json.load(r_file)["names"]
        if int(index) - 1 > len(names) - 1 or int(index) - 1 < 0:
            return "Ошибка"
        else:
            return names[int(index) - 1]

def PROV_na_udalenie():
    with open("data/names.json", "r", encoding="utf-8") as r_file:
        names = json.load(r_file)["names"]
        if len(names) == 0:
            return 0

def PROV_na_dobavlenie(n):
    with open("data/names.json", "r", encoding="utf-8") as r_file:
        names = json.load(r_file)["names"]
        if n == "":
            car = car_dict[""]
            car.DEL()
            return "Ошибка. Не была введена марка."
        if n in names:
            return "Машина успешно добавлена."

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

while True:

    print("1. Добавить автомобиль\n2. Изменить автомобиль\n3. Удалить автомобиль\n"
          "4. Информация по машине\n"
          "5. Выйти")

    car_dict = {}

    a = str(input())
    if is_number(a) == False:
        continue
    #Добавить авто
    if str(a) == '1':
        car = Car(name = input("Введите марку: "),
                  model = input("Введите модель: "),
                  color = input("Введите цвет: "),
                  L = input("Введите литраж двигателя: "),
                  price = input("Введите стоимость: "),
                  D_LF = "True",
                  D_RF = "True",
                  D_LB = "True",
                  D_RB = "True",
                  fara_l = "Выкл.",
                  fara_r = "Выкл.")
        car_dict[car.name] = car
        print(PROV_na_dobavlenie(car.name))
        print("")

    #Изменить авто
    if str(a) == '2':
        print(output())
        x = int(input("Введите номер машины: "))
        name = insex_to_name(x)
        if name not in car_dict.keys():
            car = Car()
            car.restore(name)
        else:
            car = car_dict[name]
        print("")

        n = int(input("1. Изменить марку\n2. Изменить модель\n3. Изменить цвет\n"
                      "4. Изменить литраж двигателя\n"
                      "5. Изменить стоимость\n"
                      "6. Добавить/убрать двери\n"
                      "7. Вкл./выкл. фары\n"))
        if n == 1:
            m = str(input("Введите новую марку: "))
            new_car = Car(m, car.model, car.color, car.L, car.price, car.D_LF, car.D_RF, car.D_LB, car.D_RB, car.fara_l, car.fara_r)
            car.DEL()
            car = None
            car = new_car

        if n == 2:
            md = str(input("Введите новую модель: "))
            car.model = md
            car.save()

        if n == 3:
            col = str(input("Введите новый цвет: "))
            car.color = col
            car.save()

        if n == 4:
            Lit = str(input("Введите новый литраж двигателя: "))
            if is_number(Lit) == False:
                print(f"Ошибка. {Lit} не число.")
                continue
            car.L = Lit
            car.save()

        if n == 5:
            pr = str(input("Введите новую стоимость: "))
            car.price = pr
            car.save()

        if n == 6:
            print("1. Левая передняя дверь\n"
                  "2. Правая передняя дверь\n"
                  "3. Левая задняя дверь\n"
                  "4. Правая задняя дверь\n")
            v = int(input("Введите номер двери: "))
            if v == 1:
                print("Текущее состояние двери:", car.D_LF)
                print("1. Добавить дверь\n2. Убрать дверь")
                o = int(input())
                if o == 1:
                    car.D_LF = "True"
                    car.save()
                if o == 2:
                    car.D_LF = "False"
                    car.save()
                else:
                    continue
            if v == 2:
                print("Текущее состояние двери:", car.D_RF)
                print("1. Добавить дверь\n2. Убрать дверь")
                o = int(input())
                if o == 1:
                    car.D_RF = "True"
                    car.save()
                if o == 2:
                    car.D_RF = "False"
                    car.save()
                else:
                    continue
            if v == 3:
                print("Текущее состояние двери:", car.D_LB)
                print("1. Добавить дверь\n2. Убрать дверь")
                o = int(input())
                if o == 1:
                    car.D_LB = "True"
                    car.save()
                if o == 2:
                    car.D_LB = "False"
                    car.save()
                else:
                    continue
            if v == 4:
                print("Текущее состояние двери:", car.D_RB)
                print("1. Добавить дверь\n2. Убрать дверь")
                o = int(input())
                if o == 1:
                    car.D_RB = "True"
                    car.save()
                if o == 2:
                    car.D_RB = "False"
                    car.save()
                else:
                    continue
            else:
                continue
        if n == 7:
            print("1. Левая\n"
                  "2. Правая\n")
            m = int(input("Введите номер фары: "))
            if m == 1:
                print("Текущее состояние фары:", car.fara_l)
                print("1. Вкл.\n"
                      "2. Выкл.\n")
                y = int(input())
                if y == 1:
                    car.fara_l = "Вкл."
                    car.save()
                if y == 2:
                    car.fara_l = "Выкл."
                    car.save()
                else:
                    continue
            else:
                continue
            if m == 2:
                print("Текущее состояние фары:", car.fara_l)
                print("1. Вкл.\n"
                      "2. Выкл.\n")
                y = int(input())
                if y == 1:
                    car.fara_r = "Вкл."
                    car.save()
                if y == 2:
                    car.fara_r = "Выкл."
                    car.save()
                else:
                    continue
            else:
                continue
        else:
            continue
        print("")

    #Удалить авто
    if str(a) == '3':
        if PROV_na_udalenie() == 0:
            print("Нет машин для удаления.")
            continue
        print(output())
        b = input("Введите машину: ")
        b = insex_to_name(b)
        if b == "Ошибка":
            continue
        if b in car_dict.keys():
            car: Car = car_dict[b]
            car.DEL()
        else:
            car = Car()
            car.restore(b)
            car.DEL()
        print("")

    #Информация об авто
    if str(a) == '4':
        print(output())
        z = int(input("Введите номер машины: "))
        name = insex_to_name(z)
        car = Car()
        car.restore(name)
        print(car.info())
        print("")

    #Выход из программы
    if str(a) == '5':
        exit()

    else:
        continue

print("хуй")
