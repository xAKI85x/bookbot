from stats import get_book_text, get_wordcount, convert

def main ():
    get_book_text("books/frankenstein.txt")
    char_count = get_wordcount("books/frankenstein.txt")
    gezählt = convert(char_count)
    for g in gezählt:
        print(f"{g["char"]}: {g["num"]}")

main()