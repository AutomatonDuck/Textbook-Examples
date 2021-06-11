#this program will count the diffrent combinations of poker hands from a data_file and return the probability

#open data_file
file_str = input("Enter file name: ")
while True:
    try:
        poker_file = open(file_str,'r')
        break #success, program will continue
    except IOError:
        print("Error: Cannot open file: ", file_str)
        file_str = input("Enter file name: ")


total_count = 0 #variable to hold total count of all hands
pair_count = 0 #variable to hold total count of pairs
nothin_count = 0 #variable to hold total count of nothings
two_pair_count = 0 #variable to hold total count of two pairs
three_of_a_kind_count = 0 #variable to hold total count of three of a kind
straight_count = 0 #variable to hold total count of straights
flush_count = 0 #variable to hold total count of flush
full_house_count = 0 #variable to hold total count of full houses
four_of_a_kind_count = 0 #variable to hold total count of four of a kind
straight_flush_count = 0 #variable to hold total count of straight flushes
royal_flush_count = 0 #variable to hold total count of royal flushes

#step through each line of the file
for line_str in poker_file:
    total_count +=1

    #the data contains 11 fields using commas to split data
    fields = line_str.split(',') #will split string at commas to allow reading from individual fields
    hand_rank_str = fields[-1] # gets the last field

    #need to change hand rank to int so it can be compared to a int value for if statement
    hand_rank_int = int(hand_rank_str)

    try:
        if hand_rank_int == 1:
            pair_count +=1
        elif hand_rank_int == 2:
            two_pair_count +=1
        elif hand_rank_int == 3:
            three_of_a_kind_count +=1
        elif hand_rank_int == 4:
            straight_count +=1
        elif hand_rank_int == 5:
            flush_count +=1
        elif hand_rank_int == 6:
            full_house_count +=1
        elif hand_rank_int == 7:
            four_of_a_kind_count +=1
        elif hand_rank_int == 8:
            straight_flush_count +=1
        elif hand_rank_int == 9:
            royal_flush_count +=1
        else:
            nothin_count +=1
    except ValueError:
        continue #bad line

print("Total hands on file:", total_count)
print("Hand counts by rank number: ", nothin_count, pair_count, \
    three_of_a_kind_count, straight_count, flush_count, full_house_count, \
        four_of_a_kind_count, straight_flush_count, royal_flush_count)
print("Probability:")
print(" of nothing:  {:>9.4%}".format(nothin_count/total_count))
print(" of pair:  {:>9.4%}".format(pair_count/total_count))
print(" of two pairs:  {:>9.4%}".format(two_pair_count/total_count))
print(" of three of a kind:  {:>9.4%}".format(three_of_a_kind_count/total_count))
print(" of straight:  {:>9.4%}".format(straight_count/total_count))
print(" of flush:  {:>9.4%}".format(flush_count/total_count))
print(" of full houses:  {:>9.4%}".format(full_house_count/total_count))
print(" of four of a kind:  {:>9.4%}".format(four_of_a_kind_count/total_count))
print(" of straight flush:  {:>9.4%}".format(straight_flush_count/total_count))
print(" of royal flush:  {:>9.4%}".format(royal_flush_count/total_count))