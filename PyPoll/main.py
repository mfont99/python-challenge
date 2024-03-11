
import csv                                                                  # imports
import os

row_count = 0                                                               # variables
first_candidate = True
current_candidate = ""
previous_candidate = ""
candidate_list = {}                                                         # idea to use a dictionary from AI
max_candidate = None
max_vote_count = 0

with open('Resources/election_data.csv','r') as csv_file:                   # reading in raw data
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        
        row_count += 1                                                      # count number of rows (votes)

        current_candidate = line[2]                                         # set value for current candidate

        if current_candidate in candidate_list:                             # check for duplicate string before appending to list (AI)

            candidate_list[current_candidate] += 1                          # if duplicate, increment the number of votes that candidate has

        else:
            
            candidate_list[current_candidate] = 1                           # if not duplicate, initialize a new key in the dictionary and set it equal to 1

file_path = os.path.join("analysis","results.txt")

with open(file_path,'w') as results:                                        # set up new path to export the .txt file before getting to the print statements

    print(f'Election Results\n\n----------------------------\n')
    print(f'Total Votes: {row_count}\n\n----------------------------\n')

    results.write(f'Election Results\n\n----------------------------\n')
    results.write(f'Total Votes: {row_count}\n\n----------------------------\n')

    for candidate, vote_count in candidate_list.items():                    # .items() suffix from AI to loop through keys AND values using 2 variables rather than just the keys

        vote_percentage = (vote_count / row_count) * 100

        if vote_count > max_vote_count:

            max_candidate = candidate
            max_vote_count = vote_count

        print(f'{candidate}: {vote_percentage:.3f}% ({vote_count})\n')      # had to do "with open(file_path,'w')" above so that I could write to the .txt file after each loop

        results.write(f'{candidate}: {vote_percentage:.3f}% ({vote_count})\n')

    print(f'Winner: {max_candidate}')
    results.write(f'Winner: {max_candidate}')
    