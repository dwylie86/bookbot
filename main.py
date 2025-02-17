def read_file(file_path):
    """Read the contents of a file and return them as a string.

    Parameters:
        file_path (str): The path to the file to be read

    Returns:
        str: The entire contents of the file as a string
    """
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def word_count(text):
    """Count the total number of words in a text.

    Parameters:
        text (str): The text to analyze

    Returns:
        int: The number of words in the text
    """
    words = text.split()
    return len(words)

def letter_count(text):
    """Count the frequency of letters and spaces in a text.

    Parameters:
        text (str): The text to analyze

    Returns:
        dict: A dictionary where keys are characters and values are their frequencies.
              Includes both alphabetical characters and spaces.
    """
    letter_count = {}
    for char in text.lower():
        if char.isalpha() or char.isspace():
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

def main():
    """Main function that coordinates the text analysis.
    
    Performs the following steps:
    1. Reads the book file
    2. Counts total words
    3. Analyzes character frequency
    4. Prints a report showing only alphabetical character counts
    """
    book_path = "./books/frankenstein.txt"
    text = read_file(book_path)
    num_words = word_count(text)
    char_count = letter_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for char in char_count:
        if char.isalpha():
            print(f"The '{char}' character was found {char_count[char]} times")
    print(f"--- End Report ---")

if __name__ == "__main__":
    main()