
class Car:
    
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def print_data(self):
        print("Car data: {} {}".format(self.color, self.model))   


if __name__ == "__main__":
    car = Car("blue","Nissan")
    car_two = Car("red", "Toyota")
    car.print_data()
    car_two.print_data()
    

