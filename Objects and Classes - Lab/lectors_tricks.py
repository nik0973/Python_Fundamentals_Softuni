class Car:
    cars_numbers = 0 # class attribute - може да бъде достъпен както през инстанцията, така и през класа
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car('Mercedes', 190, 1995)
# print(car1) # не е възможно достъпа до целия обект, само до неговите атрибути
# print(car1.brand) # това е възможно, тъй като ни позволява достъпа до атрибутите на обекта, но не и до самия него като цяло
car2 = Car('Fiat', 'Typo', 1990)
print(car1.brand)
car1.brand = 'BMW'
print(car1.brand)

car1.cars_numbers += 1 # променяйки клас атрибута през инстанцията car1 ние не променяме стойносттта на клас атрибута
print(car1.cars_numbers) # печатаме стойността през инстанса car1
print(Car.cars_numbers) # реално обаче виждаме че клас атрибута не се е променил
Car.cars_numbers += 1 # променяме стойността на клас атрибута извиквайки го през класа Car
print(Car.cars_numbers) # сега вече виждаме че клас атрибута си е променил стойността