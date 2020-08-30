
from prac6.guitar import Guitar

def test_guitar():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitars = Guitar(name,year,cost)
    other = Guitar("Another guitar",2013,1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitars.name,98,guitars.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name,2,guitars.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitars.name,True,guitars.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False,guitars.is_vintage()))

if __name__=='__main__':
    test_guitar()