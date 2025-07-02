from stats import get_books_text
from stats import count_words
from stats import char_count
from stats import sorted_list
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")


    book_contents = get_books_text(sys.argv[1])
    num_of_words = count_words(book_contents)
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    
    char_freq = char_count(book_contents)

    
    sorted_list(char_freq)
main()

