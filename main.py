# Игра Морской бой
# Автор: Ринчино Булат
# Курс: FPW112

import random

# Класс Корабля
class Ship:
    def __init__(self, lenght = 1, coordinates = []):
        self.__lenght = lenght # Длина корабля
        self.coordinates = coordinates # Координаты корабля [(x,y)] или [(x,y),(x1,y1)]
        self.id = 1
        self.gamer = 1
        self.status = "normal"
        self.__item_ship = []

    # установка координат
    def set_ship_coordinates(self, coordinates):
        self.coordinates = coordinates

    # установка длины корабля
    def set_lenght(self, lenght):
        self.__lenght = lenght

    # установка id корабля
    def set_id_ship(self, id_ship):
        self.id = id_ship

    # Установка статуса корабля
    def set_status_ship(self, status):
        self.status = status

    # Установка экземпляра корабля
    def set_ship_item(self):
        obj_ship = {
            "id": self.id,
            "gamer": self.gamer,
            "status": self.status,
            "coordinates": self.coordinates
        }
        self.__item_ship.append(obj_ship)

    # установка игрока
    def set_gamer(self, gamer):
        self.gamer = gamer

    # Получение длины корабля
    def get_lenght(self):
        return self.__lenght

    # Получение координат корабля
    def get_coordinates(self):
        print(self.coordinates)
        return self.coordinates

    # Получение экземпляра корабля
    def get_ship(self):
        return self.__item_ship

class Field:
    def __init__(self, ships=[], size = 6, min_distance = 2):
        self.__ships = ships
        self.__size = size
        self.__min_distance = min_distance
        self.__coordinates = []
        self.__fields=[]
        self.gamer = 1
        self.player_grid = []


    # Получение мин дистации
    def get_min_distance(self):
        return self.__min_distance

    # Установка размера поля
    def set_size(self, size):
        self.__size = size

    # Получение поля
    def get_ships(self):
        return self.__ships

    # установка игрока
    def set_field_gamer(self, gamer):
        self.gamer = gamer

    # Установка экземпляра поля
    # Объект в котором содержится данные полей игроков
    def set_field_items(self, gamer):
        self.set_field_gamer(gamer)
        obj = {
            "gamer": self.gamer,
            "field": self.__ships # Добавляем координаты кораблей
        }
        # Создаем пустую сетку игроков
        grid = {
            "gamer": self.gamer,
            "grid": {}  # Пример содержимого 'grid': {(0, 0): 'o', (0, 1): 'o', (0, 2): 'o'}
        }
        self.__fields.append(
            obj
        )
        self.player_grid.append(
            grid
        )

    # Получение экземпляра поля
    def get_item_fields(self):
        return self.__fields

    # Установка случайным образом координат кораблей
    # * @param size - размер карты в клетках, целое число
    # * @param lenght - размер корабля в клетках, целое число
    def set_ship(self, size, length, min_distance):
        i = 1
        while True:
            # Случайный выбор координат
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                # Установка начальных координат
                x = random.randint(0, size - length)
                y = random.randint(0, size - 1)
                # Добавление по оси х клеток
                self.__coordinates = [(x+i, y) for i in range(length)]
            else:
                # Установка начальных координат
                x = random.randint(0, size - 1)
                y = random.randint(0, size - length)
                # Добавление по оси у клеток
                self.__coordinates = [(x, y+i) for i in range(length)]
            # Проверка полученных координат
            if self.is_valid_location(self.__coordinates, min_distance):
                # возвращаем координаты корабля на поле [(x,y),(x,y)]
                return self.__coordinates

    # Проверка расположения кораблей
    # *@param ship - Координаты корабля [(x,y)]
    # *@param min_distance - Минимальная дистанция (по умолчанию 2)
    def is_valid_location(self, ship, min_distance = 2):
        self.__coordinates = ship
        for x, y in self.__coordinates:
            if x < 0 or x >= self.__size or y < 0 or y >= self.__size:
                return False
            for other_ship in self.__ships:
                for other_x, other_y in other_ship:
                    if abs(x - other_x) < min_distance and abs(y - other_y) < min_distance:
                        return False
        return True

    # Установка кораблей на поле
    def set_ships(self, gamer, obj_ship, ships, a = 1, b = 2, c = 3):
        id_ship = 1
        self.__ships = ships
        while len(ships) < 1:
            ship = self.set_ship( self.__size, c, self.__min_distance)
            ships.append(ship)
            obj_ship.set_id_ship(id_ship)
            obj_ship.set_gamer(gamer)
            obj_ship.set_status_ship("normal")
            obj_ship.set_ship_coordinates(ship)
            obj_ship.set_ship_item()
            id_ship = id_ship +1


        while len(ships) < 3:
            ship = self.set_ship( self.__size, b, self.__min_distance)
            ships.append(ship)
            obj_ship.set_id_ship(id_ship)
            obj_ship.set_gamer(gamer)
            obj_ship.set_status_ship("normal")
            obj_ship.set_ship_coordinates(ship)
            obj_ship.set_ship_item()
            id_ship = id_ship +1

        while len(ships) < 7:
            ship = self.set_ship( self.__size, a, self.__min_distance)
            ships.append(ship)
            obj_ship.set_id_ship(id_ship)
            obj_ship.set_gamer(gamer)
            obj_ship.set_status_ship("normal")
            obj_ship.set_ship_coordinates(ship)
            obj_ship.set_ship_item()
            id_ship = id_ship +1

    # Запись выстрела в сетку игрока
    def set_shot_grid(self, gamer, coord=(0,0)):
        player_grids = self.player_grid

        # Выбираем сетку игрока, будем туда записывать метки кораблей
        for gamer_grid in player_grids:
            if gamer_grid['gamer'] == gamer:
                grid = gamer_grid['grid']
                if grid[coord] == "■":
                    print(grid[coord])
                    grid[coord] = "X"
                else:
                    print(grid[coord])
                    grid[coord] = "T"
                print(player_grids)



    # Запись сетки
    def set_grids(self, gamer):
        # Получаем сетку, сюда будем записывать все выстрелы
        player_grids = self.player_grid
        gamer_fields = self.get_item_fields()
        # Выбираем игрока, и координаты его кораблей
        for gamer_field in gamer_fields:
            if gamer_field['gamer'] == gamer:
                ships = gamer_field['field']

        # Выбираем сетку игрока, будем туда записывать метки кораблей
        for gamer_grid in player_grids:
            if gamer_grid['gamer'] == gamer:
                grid = gamer_grid['grid']
        # тут мы проходим по всем кординатам
        for x in range(self.__size):
            for y in range(self.__size):
                if any((x, y) in ship for ship in ships):
                    grid[(x,y)] = "■"
                else:
                    grid[(x,y)] = "o"

    # получение сетки
    def get_grids(self):
        return self.player_grid

    # Вывод поля на экран
    def get_field(self, gamer):
        # из self.fields мне нужно получить поля игроков
        gamer_fields = self.get_item_fields()
        # Выбираем игрока, и координаты его кораблей
        for gamer_field in gamer_fields:
            if gamer_field['gamer'] == gamer:
                ships = gamer_field['field']
                # попробуем заменить на player_grid где будут указаны все координаты
                # ships = player_grid['grid']

        # Вывод сетки на экран, выводим вертикальные линии
        for i, f in enumerate(range(self.__size+1)):
            if i == self.__size:
                print(f,"|")
            elif i == 0:
                print(" ","|",end=" ")
            else:
                print(f,"|",end=" ")
        # тут мы проходим по всем кординатам, если совпадает, то выводим О
        for x in range(self.__size):
            print(x+1,"|", end=" ")
            for y in range(self.__size):
                if any((x, y) in ship for ship in ships):
                    print("O", "|", end=" ")
                else:
                    print("-", "|", end=" ")
            print()

# установка поля
appField = Field([], 6, 2)

# Установка кораблей
ship = Ship()
for i in range(2):
    appField.set_ships( i+1, ship, [], 1, 2, 3)
    appField.set_field_items(i+1)

# Получение кораблей
appField.get_ships()

# Вывод поля
print("Поле игрока 1")
appField.get_field(1)

print("Поле игрока 2")
appField.get_field(2)

appField.set_grids(1)
appField.set_grids(2)


# print("ship.get_ship():", ship.get_ship())

# fields_gamers = appField.get_item_fields()

# print("appField.get_item_fields():", appField.get_item_fields()) : [
# {
#   'gamer': 1,
#   'field': [[(3, 3), (3, 4), (3, 5)], [(2, 0), (3, 0)], [(1, 4), (1, 5)], [(0, 0)], [(5, 1)], [(1, 2)], [(5, 3)]]
# },
# {
#   'gamer': 2,
#   'field': [[(0, 1), (0, 2), (0, 3)], [(3, 2), (4, 2)], [(4, 4), (5, 4)], [(2, 4)], [(5, 0)], [(0, 5)], [(3, 0)]]
# }
# ]

# Создаем словарь, который будет хранить информацию о попаданиях и потоплениях кораблей
# Ключи словаря - это координаты клеток, значения - True для попадания и False для промаха
# Все это надо засунуть в классы.
# hits = {coord: False for gamer in fields_gamers for ship in gamer['field'] for coord in ship}

# Определяем, какой игрок сейчас ходит (первый или второй)
current_gamer = 1
appField.set_shot_grid(current_gamer, (0,2))
# print(appField.get_grids())
# Получаем координаты от пользователя

# Проверяем попадание в игрока 2

# если попал, отмечаем координату символом попал


# Отладка кода для размещения кораблей

'''
SIZE = 6
MIN_DISTANCE = 2
ships = []

# Проверка расположения кораблей
def is_valid_location(ship):
    for x, y in ship:
        if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
            return False
        for other_ship in ships:
            for other_x, other_y in other_ship:
                if abs(x - other_x) < MIN_DISTANCE and abs(y - other_y) < MIN_DISTANCE:
                    return False
    return True

# генерируем корабль случайным образом
def generate_ship(length):
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            x = random.randint(0, SIZE - length)
            y = random.randint(0, SIZE - 1)
            ship = [(x+i, y) for i in range(length)]
        else:
            x = random.randint(0, SIZE - 1)
            y = random.randint(0, SIZE - length)
            ship = [(x, y+i) for i in range(length)]
        if is_valid_location(ship):
            return ship



while len(ships) < 1:
    ship = generate_ship(3)
    ships.append(ship)

while len(ships) < 3:
    ship = generate_ship(2)
    ships.append(ship)

while len(ships) < 7:
    ship = generate_ship(1)
    ships.append(ship)



# Вывод сетки на экран
for i, f in enumerate(range(SIZE+1)):
    if i == SIZE:
        print(f,"|")
    elif i == 0:
        print(" ","|",end=" ")
    else:
        print(f,"|",end=" ")

for x in range(SIZE):
    print(x+1,"|", end=" ")
    for y in range(SIZE):
        if any((x, y) in ship for ship in ships):
            print("O", "|", end=" ")
        else:
            print(".", "|", end=" ")
    print()

print("ships содержит координаты")
print(ships)

'''


