def main():
    print("--- Begin report of books/frankenstein.txt ---")

    text = read_file('books/frankenstein.txt')
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")

    letter_report = get_letter_report(text)
    letter_report.sort(reverse=True, key=sort_on)
    
    for item in letter_report:
        print(f"The '{item['letter']}' character was found {item['count']} times")

    print("\n--- End report ---")

def read_file(path):
    with open(path, 'r') as file:
        return file.read()
    
def get_num_words(text):
    return len(text.split())

def get_letter_report(text):
    text = text.lower()
    letter_count = {}

    for letter in text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    
    letter_report = []
    for letter, count in letter_count.items():
        letter_report.append({"letter": letter, "count": count})

    return letter_report

def sort_on(dict):
    return dict["count"]
    


main()