class Transport:
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    def __str__(self) -> str:
        """
        Представление всей информации для вывода в методе print()
        """
        return (f"Transport: Brand {self.brand}, Year {self.year}, Number {self.number}, Coordinates {self.coordinates},"
                f" Speed {self.speed}")

    @property
    def coordinates(self) -> tuple:
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates: tuple):
        self._coordinates = coordinates

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, speed: int):
        self._speed = speed

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        self._brand = brand

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year: int):
        self._year = year

    @property
    def number(self) -> str:
        return self._number

    @number.setter
    def number(self, number: str):
        self._number = number

    def is_in_area(self, pos_x, pos_y, length, width) -> bool:
        """
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        """
        x, y = self.coordinates
        if pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width:
            return True
        return False


class Passenger:
    def __init__(self):
        self._passengers_capacity = None
        self._number_of_passengers = None

    @property
    def passengers_capacity(self) -> int:
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity: int):
        self._passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self) -> int:
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers: int):
        self._number_of_passengers = number_of_passengers


class Cargo:
    def __init__(self):
        self._carrying = None

    @property
    def carrying(self) -> int:
        return self._carrying

    @carrying.setter
    def carrying(self, carrying: int):
        self._carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, height: int):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Auto(Transport):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, port: str):
        super().__init__(coordinates, speed, brand, year, number)
        self._name = name
        self._port = port

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        self._port = value


class Car(Auto):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        super().__init__(coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        super().__init__(coordinates, speed, brand, year, number)


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        super().__init__(coordinates, speed, brand, year, number)


class Boat(Ship):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, port: str):
        super().__init__(coordinates, speed, brand, year, number)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        super().__init__(coordinates, speed, brand, year, number)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        super().__init__(coordinates, speed, brand, year, number)


class Seaplane(Plane, Ship):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, port: str):
        super().__init__(coordinates, speed, brand, year, number, port)


def test_transport() -> None:
    """
    Проверка функционала класса Transport.
    """
    coordinates = (10, 20)
    speed = 100
    brand = "Toyota"
    year = 2022
    number = "ABC123"

    vehicle = Transport(coordinates, speed, brand, year, number)
    assert vehicle.coordinates == coordinates
    assert vehicle.speed == speed
    assert vehicle.brand == brand
    assert vehicle.year == year
    assert vehicle.number == number

    new_coordinates = (15, 25)
    vehicle.coordinates = new_coordinates
    assert vehicle.coordinates == new_coordinates

    new_speed = 120
    vehicle.speed = new_speed
    assert vehicle.speed == new_speed

    new_brand = "Honda"
    vehicle.brand = new_brand
    assert vehicle.brand == new_brand

    new_year = 2023
    vehicle.year = new_year
    assert vehicle.year == new_year

    new_number = "XYZ789"
    vehicle.number = new_number
    assert vehicle.number == new_number

    assert vehicle.is_in_area(5, 15, 20, 30) is True
    assert vehicle.is_in_area(30, 40, 10, 10) is False


def test_passenger() -> None:
    """
    Проверка функционала класса Passenger.
    """
    passenger = Passenger()
    passenger.passengers_capacity = 100
    assert passenger.passengers_capacity == 100

    passenger.number_of_passengers = 50
    assert passenger.number_of_passengers == 50


def test_cargo() -> None:
    """
    Проверка функционала класса Cargo.
    """
    cargo = Cargo()
    cargo.carrying = 2000
    assert cargo.carrying == 2000


def test_plane() -> None:
    """
    Проверка функционала класса Plane.
    """
    coordinates = (30, 40)
    speed = 500
    brand = "Boeing"
    year = 2015
    number = "DEF456"
    height = 10000

    plane = Plane(coordinates, speed, brand, year, number, height)
    assert plane.height == height


if __name__ == '__main__':
    test_transport()
    test_passenger()
    test_cargo()
    test_plane()
