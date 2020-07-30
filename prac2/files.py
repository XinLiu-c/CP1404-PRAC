# Write code that asks the user for their name,
# then opens a file called "name.txt" and writes that name to it.
name=input("Please enter your name: ")
name_files=open("name.txt","w")
name_files.close()

# Write code that opens "name.txt" and reads the name (as above) then prints.
name_files=open("name.txt","r")
print("Your name is ",name)
name_files.close()

# Write code that opens "numbers.txt",
# reads only the first two numbers and adds them together then prints the result.
num_files=open("numbers.txt","r")
first_line_str=num_files.readline()
second_line_str=num_files.readline()
sum=int(first_line_str)+int(second_line_str)
print(sum)
num_files.close()

# write a fourth block of code that prints the total for all lines in numbers.txt.
num_files=open("numbers.txt","r")
all_lines_str=num_files.readlines()
print(all_lines_str)
num_files.close()