from stats import get_book_text, get_wordcount, convert
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main ():
    get_book_text(sys.argv[1])
    char_count = get_wordcount(sys.argv[1])
    gezählt = convert(char_count)
    for g in gezählt:
        print(f"{g["char"]}: {g["num"]}")

main()