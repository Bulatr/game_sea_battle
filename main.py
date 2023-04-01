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
        gamer_fields = self.get_item_fields()
        # Выбираем сетку игрока, будем туда записывать метки кораблей
        gamer_field = gamer_fields[gamer - 1]
        ships = gamer_field['field']
        gamer_grid = player_grids[gamer - 1]
        grid = gamer_grid['grid']
        if any( coord in ship for ship in ships):
            grid[coord] = "X" # Попадание
        else:
            grid[coord] = "T" # Промах

    def get_player_grid(self):
        return self.player_grid


    # Вывод сетки игрока
    def get_grid_player(self, player):
        print(f"Карта игрока {player}")
        player_grids = self.player_grid
        # Вывод сетки на экран, выводим вертикальные линии
        for i, f in enumerate(range(self.__size+1)):
            if i == self.__size:
                print(f,"|")
            elif i == 0:
                print(" ","|",end=" ")
            else:
                print(f,"|",end=" ")

        for gamer_grid in player_grids:
            if gamer_grid['gamer'] == player:
                grid = gamer_grid['grid']
                for x in range(self.__size):
                    print(x+1,"|", end=" ")
                    for y in range(self.__size):
                        print(grid[(x,y)],"|",end=" ")
                    print()

    # Запись сетки, первоначальная установка
    def set_grids(self):
        # Получаем сетку, сюда будем записывать все выстрелы
        player_grids = self.get_player_grid()
        gamer_fields = self.get_item_fields()
        # Выбираем игрока, и координаты его кораблей
        gamers = [1,2]
        for gamer in gamers:
            gamer_field = gamer_fields[gamer-1]
            ships = gamer_field['field']
            # Выбираем сетку игрока, будем туда записывать метки кораблей
            gamer_grid = player_grids[gamer-1]
            grid = gamer_grid['grid']
            # тут мы проходим по всем кординатам
            for x in range(self.__size):
                for y in range(self.__size):
                    if any((x, y) in ship for ship in ships):
                        grid[(x,y)] = "o"
                    else:
                        grid[(x,y)] = "o"


    # получение сетки
    def get_grids(self):
        return self.player_grid

    # Проверка количества клеток кораблей, условие выйгрыша
    # После каждого хода проверяем количество подбитых клеток
    def check_ships_in_grid_gamer(self):
        player_grids = self.player_grid
        cells_player_1 = 0
        cells_player_2 = 0
        for gamer_grid in player_grids:
            grid = gamer_grid['grid']
            player = gamer_grid["gamer"]
            # тут мы проходим по всем кординатам
            for x in range(self.__size):
                for y in range(self.__size):
                    if grid[(x,y)] == "X":
                        if player == 1:
                            cells_player_1 += 1
                        else:
                            cells_player_2 += 1

        # Проверяем количество подбитых клеток
        if cells_player_1 > cells_player_2 and cells_player_1 == 11:
            return 2
        elif cells_player_2 > cells_player_1 and cells_player_2 == 11:
            return 1
        else:
            return False

    # Функция которая просит ввести координаты
    def input_coord(self, player):
        gx = True
        gy = True
        player_grids = self.player_grid
        t = True
        while t:
            while gx:
                try:
                    shot_x = int(input("Введите координату x для выстрела: "))
                    if shot_x < 1 or shot_x > self.__size:
                        print(f"Введите корректные значения, от 1 до {self.__size}")
                        continue
                    gx = False

                except ValueError:
                    print(f"Введите корректные значения, от 1 до {self.__size}")
                    continue

            while gy:
                try:
                    shot_y = int(input("Введите координату y для выстрела: "))
                    if shot_y < 1 or shot_y > self.__size:
                        print(f"Введите корректные значения, от 1 до {self.__size}")
                        continue
                    gy = False

                except ValueError:
                    print(f"Введите корректные значения, от 1 до {self.__size}")
                    continue
            # Проверяем координаты на повтор
            for player_grid in player_grids:
                # Меняем местами игрока, так как проверяем на сетке оппонента
                if player_grid["gamer"] == player:
                    grid = player_grid["grid"]
                    if grid[(shot_x-1,shot_y-1)] == "X" or grid[(shot_x-1,shot_y-1)] == "T":
                        print("Вы уже стреляли по этим координатам")
                        gx = True
                        gy = True
                    else:
                        t = False
        return (shot_x-1,shot_y-1)

    # Проверка попадания по кораблю
    def check_shot_ships(self, player, coord):
        gamer_fields = self.get_item_fields()
        # Выбираем оппонента
        if player == 1:
            player = 2
        else:
            player = 1
        for gamer_field in gamer_fields:
            if gamer_field['gamer'] == player:
                ships = gamer_field['field']
                if any( coord in ship for ship in ships):
                    print("Попадание")
                    return True
                else:
                    print("Промах")
                    return False

# установка поля
appField = Field([], 6, 2)

# Установка кораблей
ship = Ship()
for i in range(2):
    appField.set_ships( i+1, ship, [], 1, 2, 3)
    appField.set_field_items(i+1)

# Получение кораблей
appField.get_ships()
appField.set_grids()

# Определяем, какой игрок сейчас ходит первый
current_gamer = 1

# Меняем игрока
def reverse_player(player):
    if player == 1:
        return 2
    else:
        return 1

# Создаем бесконечный цикл
check_end_game = True

while check_end_game:
    print(f"Ходит игрок {current_gamer}")
    coord = appField.input_coord(reverse_player(current_gamer))
    appField.set_shot_grid(reverse_player(current_gamer), coord)
    win = appField.check_ships_in_grid_gamer()
    if win:
        print(f"Игрок {win} победил")
        appField.get_grid_player(reverse_player(current_gamer))
        print()
        appField.get_grid_player(current_gamer)
        break
    if appField.check_shot_ships(current_gamer, coord):
        print(f"Игрок {current_gamer} продолжает ход")
        print()
        appField.get_grid_player(reverse_player(current_gamer))
        print()
        appField.get_grid_player(current_gamer)
        print()
    else:
        print()
        appField.get_grid_player(reverse_player(current_gamer))
        print()
        appField.get_grid_player(current_gamer)
        current_gamer = reverse_player(current_gamer)
        print()
    


# appField.get_item_fields() : [
# {
#   'gamer': 1,
#   'field': [[(3, 3), (3, 4), (3, 5)], [(2, 0), (3, 0)], [(1, 4), (1, 5)], [(0, 0)], [(5, 1)], [(1, 2)], [(5, 3)]]
# },
# {
#   'gamer': 2,
#   'field': [[(0, 1), (0, 2), (0, 3)], [(3, 2), (4, 2)], [(4, 4), (5, 4)], [(2, 4)], [(5, 0)], [(0, 5)], [(3, 0)]]
# }
# ]

