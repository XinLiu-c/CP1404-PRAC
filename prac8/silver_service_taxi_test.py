
from prac8.silver_service_taxi import ServiceTaxi

def main():
    taxi = ServiceTaxi("Test taxi",100,1.23,3)
    taxi.drive(20)
    print(taxi)
    print(taxi.get_fare())

main()