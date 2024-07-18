def read_and_print(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def main():
    print(word_count(read_and_print("books/frankenstein.txt")))
    

main()
