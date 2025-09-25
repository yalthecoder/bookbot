
from stats import get_num_words
from stats import get_num_chars
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else :
    book_to_read = sys.argv[1]

    def get_book_text(book):
        with open(book) as f:
            print(f.read())

    def main():
        num_chars = get_num_chars(book_to_read)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_to_read}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(book_to_read)} total words")
        print("--------- Character Count -------")
        num_chars_sorted = sorted(num_chars.items(), key=lambda item: item[1], reverse=True)
        for i in num_chars_sorted:
            print(f"{i[0]}: {i[1]}")
    
    main()
