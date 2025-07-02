
def get_books_text(path):
    with open(path) as f:
        book_contents = f.read()
        return book_contents
    
def count_words(string):
    book_split = string.split()
    count = len(book_split)
    return count

def char_count(book_contents):
    char_count = {}
    for i in book_contents:
        low = i.lower()
        if low in char_count:
            char_count[low] += 1
        else:
            char_count[low] = 1
    return char_count

def sorted_list(char_count):
    list_of_dicts = [{"char":key, "num": value} for key, value in char_count.items()]
    def sort_on(items):
        return items["num"]
    
    list_of_dicts.sort(reverse=True, key=sort_on)

    for entry in list_of_dicts:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")




