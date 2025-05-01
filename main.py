from stats import get_num_words
from stats import get_num_letters
from stats import get_book_text
from stats import get_sorted_dic
import sys

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    # filepath = "books/frankenstein.txt"
    num_words = get_num_words(filepath)
    text = get_book_text(filepath)
    letters = get_num_letters(text)
    sorted_list = get_sorted_dic(letters)



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")



main()

