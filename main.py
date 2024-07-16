def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    generate_report(book_path, word_count, chars_sorted_list)

def count_words(text):    
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]
    
def generate_report(book_path, word_count, chars_sorted_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    
    print("--- End Report ---")

main()