"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    list_data = []
    input_file = open(FILENAME,'r')
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        list_data.append(parts)
    input_file.close()
    return list_data

def subject_details(parts):
    for list in parts:
        print('{} is taught by {:12} and has {:3} students'.format(list[0],list[1],list[2]))
main()