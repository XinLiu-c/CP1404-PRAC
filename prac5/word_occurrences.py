
def main():
    text=input("Please enter your text: ")
    new_text=text.split()
    word_to_count={}
    for word in new_text:
        word_to_count[word]=word_to_count.get(word,0)+1
    for k,v in sorted(word_to_count.items()):
        print("{:10} : {}".format(k,v))
main()


