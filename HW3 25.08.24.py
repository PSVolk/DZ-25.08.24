import json
import pickle

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def set_name(self, new_name):
        self.name = new_name

    def set_opening_date(self, new_date):
        self.opening_date = new_date

    def set_country(self, new_country):
        self.country = new_country

    def set_city(self, new_city):
        self.city = new_city

    def set_capacity(self, new_capacity):
        self.capacity = new_capacity

    def display_info(self):
        print(f"Название стадиона: {self.name}")
        print(f"Дата открытия: {self.opening_date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity}")

    def to_json(self):
        data = {
            "name": self.name,
            "opening_date": self.opening_date,
            "country": self.country,
            "city": self.city,
            "capacity": self.capacity
        }
        return json.dumps(data)

    def from_json(self, json_data):
        data = json.loads(json_data)
        self.name = data["name"]
        self.opening_date = data["opening_date"]
        self.country = data["country"]
        self.city = data["city"]
        self.capacity = data["capacity"]

    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)

stadium = Stadium("Стадион Зенит", "2017-08-22", "Россия", "Санкт-Петербург", 67800)


json_data = stadium.to_json()
print(json_data)

new_stadium = Stadium("", "", "", "", 0)
new_stadium.from_json(json_data)
new_stadium.display_info()

pickle_data = stadium.to_pickle()
print(pickle_data)

unpacked_stadium = Stadium.from_pickle(pickle_data)
unpacked_stadium.display_info()
