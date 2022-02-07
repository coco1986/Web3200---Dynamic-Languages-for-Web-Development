class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant is named " + self.restaurant_name + ". Go here if you like " + self.cuisine_type + ".")

    def __str__(self):
        string_object = "The restaurant is open!!!!"
        return string_object


class IceCreamStand(Restaurant):
    def __init__(self, parlor, flavors):
        super().__init__(parlor, flavors)
        self.parlor = parlor
        self.flavors = flavors

    def display_flavors(self):
        print("At this ice cream stand named " + self.parlor + " we serve the following flavors: " + self.flavors + ".\n")

if __name__ == '__main__':
    restaurant = Restaurant("Emilios", "Italian")
    restaurant.describe_restaurant()
    restaurant.__str__()
    print(restaurant)

    parlor = IceCreamStand("Baskin Robbins", "Ice Cream")
    parlor.describe_restaurant()

    parlor2 = IceCreamStand("Baskin Robbins", "Chocolate, Vanilla, and Strawberry")
    parlor2.display_flavors()

