from get_temperature import Temperature


class Calorie:
    # BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature

    def __init__(self, temperature, weight, height, age):
        self.age = age
        self.weight = weight
        self.height = height
        self.temperature = temperature

    def calculate(self):
        bmr = 10 * int(self.weight) + 6.25 * int(self.height) - 5 * int(self.age) + 5 - 10 * float(self.temperature)
        return bmr


if __name__ == "__main__":
    temperature = Temperature(country="italy", city="rome").get_temp()
    calorie = Calorie(weight=84, height=185, age=19, temperature=temperature)
    print(calorie.calculate())