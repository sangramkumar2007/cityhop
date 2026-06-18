class Trip:
    def __init__(self, distance, ride_type, is_peak_hour):
        self.__distance = distance
        self.__ride_type =ride_type
        self.__is_peak_hour = is_peak_hour
    def get_distance(self):
        return self.__distance
    def get_ride_type(self):
        return self.__ride_type
    def get_is_peak_hour(self):
        return self.__is_peak_hour
    def calculate_price(self):
        if self.__ride_type == "Standard":
            price = self.__distance * 1.5
        else:
            price = self.__distance * 2.5
        
        if self.__is_peak_hour:
            price += 5
        return price
    
trip1 = Trip(10.0, "Standard", True)
trip2 = Trip(5.5, "Premium", False)
trip3 = Trip(3.0, "Standard", False)

trips = [trip1, trip2, trip3]
total_distance = 0
total_fare = 0
total_points = 0

for trip in trips:
    total_distance += trip.get_distance()
    total_fare += trip.calculate_price()
    
    if trip.get_ride_type() == "Premium":
        total_points += trip.get_distance() * 2
    else: 
        total_points += trip.get_distance()
print("Total Distance Traveled:", total_distance)
print("Total Fare Due:  rupees", total_fare)
print("Total Loyalty Points Earned:", total_points)


