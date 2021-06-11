# This program will parse through a sample of the english dictionary using a .txt file and return words that the vowels 'aeiou' in that order.

#open the file
try:
    data_file = open("words.txt", 'r')
except FileNotFoundError:
    print("File was not found, Ensure that the file is in the current directory")
    print("or enter the entire path of the file")
    print("Exiting with error code 1")
    exit(1)

#parse the file and print the contents of the file
# for line_string in data_file:
#     print(line_string) #this will print with additional white space because of carriage return

#removes whitespace and makes word lower case
def clean_words(word):
    #.strip() will remove extra whitespace after word
    return word.strip().lower()

#finds the vowles in a string
def get_vowels(word):
    vowels_str = "aeiou"
    vowels_In_Word = ""
    for char in word:
        if char in vowels_str:
            vowels_In_Word += char
    return vowels_In_Word


#main

for word in data_file: #for each word in data_file
    word = clean_words(word)
    #will skip word if too small to hold all vowels
    if len(word) <= 6:
        continue
    #check if vowels are present and in order
    vowels_str = get_vowels(word)
    if vowels_str == 'aeiou':
        print(word)