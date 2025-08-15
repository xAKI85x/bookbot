def get_book_text(f):
    with open(f) as text:
        print(f"Found {len(text.read().split())} total words")

def get_wordcount(f):
    count = {}
    with open(f) as text:
        for i in text.read().lower().split():
            for a in i:
                if a in count:
                    count[a] += 1
                else:
                    count[a] = 1                    
    return count

def sort_on(sortiert):
    return sortiert["num"]

def convert(char_count):
    liste = []
    alphaber = []
    for i in char_count:
        if i.isalpha():
            liste.append({"char" : i,"num" : char_count[i]})
    liste.sort(reverse=True, key=sort_on)
    return liste


        