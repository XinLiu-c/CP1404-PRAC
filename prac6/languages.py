
from prac6.programming_language import programminglanguage

def main():
    ruby = programminglanguage("Ruby", "Dynamic", True, 1995)
    python = programminglanguage("Python", "Dynamic", True, 1991)
    visual_basic = programminglanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()