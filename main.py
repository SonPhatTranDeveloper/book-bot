from typing import Counter


def main():
    # Open the book text file
    with open("books/frankenstein.txt", "r") as file:
        # Read the file content into string
        file_content = file.read() 

        # Split the content into words
        words = file_content.split()

        # Convert the string into lower case and find the word count
        word_count = Counter([character.lower() for character in file_content if character.isalpha()])  
        
        # Convert to dictionary of name and count
        word_dicts = [
            {
                "name": word,
                "count": word_count[word]
            } for word in word_count
        ]

        # Sort the list based on the count
        word_dicts.sort(key=lambda x: x["count"], reverse=True)

        # Display the result
        print("--------- BEGIN OF ANALYSIS RESULT FOR books/frankenstein.txt ---------")
        print(f"There are {len(words)} words in the document")

        for item in word_dicts:
            name = item["name"]
            count = item["count"]
            print(f"The '{name}' character appears in the document {count} times")


if __name__ == "__main__":
    main()