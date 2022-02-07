from my_package import fooFunc
from my_package import Restaurant, IceCreamStand

fooFunc()

restaurant = Restaurant("Le Petit Paris", "French")
restaurant.describe_restaurant()
restaurant.__str__()
print(restaurant)

parlor = IceCreamStand("Friendlies", "Ice Cream")
parlor.describe_restaurant()

parlor2 = IceCreamStand("Friendlies", "Rocky Road, Orange Sherbert")
parlor2.display_flavors()