def main():
    print(f"Begin analyzing books/frankenstein.txt")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_count = get_chars(text)
    

def get_words():
    count = 0
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    print(words)
    for word in words:
        count += 1
    print(count)

def sort_on(chars):
    return chars["num"]

    

def get_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1

    def get_count(item):
        return item[1]
    
    sorted_chars = sorted(chars.items(), key=get_count, reverse=True)
    for letter, count in sorted_chars:
        print(f"Letter '{letter}' appears {count} times.")
    return sorted_chars

    
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


