def get_input():
    sentence=input("enter sentence")
    return sentence
def word_counter(sentence):
    words = sentence.split()
# Create a dictionary to store word counts
    word_count = {}
# Loop through each word and count occurrences
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def main():
    sentence = input("Enter a sentence: ")
# Call the word_counter function
    count = word_counter(sentence)
    for word, count in count.items():
        print(f"'{word}': {count}")

main()