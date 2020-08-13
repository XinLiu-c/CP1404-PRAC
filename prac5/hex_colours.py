def main():
    hex_colours = {"beige": "#f5f5dc", "coral": "#ff7f50", "firebrick": "#b22222", "gainsboro": "#dcdcdc",
                   "gray": "#bebebe", "lavender": "#e6e6fa", "khaki": "#f0e68c", "light": "#eedd82", "linen": "#faf0e6",
                   "magenta": "#ff00ff"}

    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        if colour_name in hex_colours:
            print(colour_name, "is", hex_colours[colour_name])
            break
        else:
            print("Invalid colour name.")
            colour_name = input("Enter colour name: ").lower()


main()
