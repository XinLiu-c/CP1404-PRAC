
from prac8.taxi import Taxi

class ServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self,name,fuel,price_per_km,fanciness):
        super().__init__(name,fuel,price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(),self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()