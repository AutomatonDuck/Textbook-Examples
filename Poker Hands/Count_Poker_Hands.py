#this program will count the diffrent combinations of poker hands from a data_file and return the probability

#open data_file
try:
    poker_file = open("poker-hand-testing.csv", 'r')
except FileNotFoundError:
    print("File was not found, Ensure that the file is in the current directory")
    print("or enter the entire path of the file")
    print("Exiting with error code 1")
    exit(1)

total_count = 0 #variable to hold total count of all hands
pair_count = 0 #variable to hold total count of pairs

#step through each line of the file
for line_str in poker_file:
    total_count +=1

    #the data contains 11 fields using commas to split data
    fields = line_str.split(',') #will split string at commas to allow reading from individual fields
    hand_rank_str = fields[-1] # gets the last field

    #need to change hand rank to int so it can be compared to a int value for if statement
    hand_rank_int = int(hand_rank_str)

    if hand_rank_int == 1:
        pair_count +=1


print("Total hands on file:", total_count)
print("Count of pair hands: ", pair_count)