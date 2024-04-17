def count_words(text):
   
    # Check for empty input
    if not text.strip():
        return 0

    # Split the text into words and return the count
    words = text.split()
    return len(words)

def main():
    # User input
    user_input = input("Enter a sentence or paragraph: ")

    # Count words and display the result
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()