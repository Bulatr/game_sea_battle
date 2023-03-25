# Игра Морской бой
# Автор: Ринчино Булат
# Курс: FPW112

import random

# Класс Корабля
class Ship:
    '''
    Класс Ship - Корабль
    Свойства:
    size - размер корабля
    coordinates - Координаты корабля (x,y)
    status - Статус корабля (damaged - поврежден, sank - потоплен)
    whole_cells - Количество целых клеток
    id_ship - id корабля (уникальный номер)
    gamer - сторона игрок или компьютер (user, computer)
    Методы
    set_ship - Создание корабля
    set_hitting_ship - Установка попадания в корабль
    get_status_ship - Получение статуса корабля, возвращвет damaged - поврежден, sank - потоплен
    '''
    def __init__(self, size, coordinates, status, whole_cells, id_ship, gamer) -> None:
        self._size = size
        self._coordinates = coordinates
        self._status = status
        self._whole_cells = whole_cells
        self._id_ship = id_ship
        self._gamer = gamer

    # Создание корабля
    def set_ship(self,coordinates):
        pass

    # установка попадания в корабль
    def set_hitting_ship(self, coordinates):
        pass

    # Получение статуса корабля
    def get_status_ship(self,id_ship):
        pass

# Класс Field
class Field:
    def __init__(self, grid_size, gamer) -> None:
        self._grid_size = grid_size
        self._gamer = gamer
        self._grid = {
            "player": self._gamer,
            "grid":[]
        }

    # Создание пустого поля
    def set_grid(self, grid_size, gamer):
        self._grid_size = grid_size
        self._gamer = gamer

        grid_size = self._grid_size 
        grid = []
        self._grid = {
            "player": self._gamer,
            "grid": grid
        }
        # Создание пустой сетки
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                row.append("0")
            grid.append(row)

        return self._grid
    
    # Создание поля игрока
    def set_grid_player(self, gamer, grid):
        pass

# Отладка кода для размещения кораблей


SIZE = 6
MIN_DISTANCE = 2
ships = []

def is_valid_location(ship):
    for x, y in ship:
        if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
            return False
        for other_ship in ships:
            for other_x, other_y in other_ship:
                if abs(x - other_x) < MIN_DISTANCE and abs(y - other_y) < MIN_DISTANCE:
                    return False
    return True

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
for x in range(SIZE):
    for y in range(SIZE):
        if any((x, y) in ship for ship in ships):
            print("O", end=" ")
        else:
            print(".", end=" ")
    print()




