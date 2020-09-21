import shutil
import os


def main():

    os.chdir('Lyrics/Christmas')

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        # print("Renaming {} to {}".format(filename, new_name))




def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    parts = ''
    name=filename.split(' ')

    for i in name:
        i=i[0].upper() + i[1:]
        parts += i

    new_parts=parts.split('.')
    new_parts[1]='txt'

    new_name =''
    for i in new_parts[0]:
        if i.isupper():
            i='_'+i
        new_name += i

    new_name = new_name[1:]
    new_name = new_name + '.txt'
    print(new_name)
    # return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))



main()
# demo_walk()