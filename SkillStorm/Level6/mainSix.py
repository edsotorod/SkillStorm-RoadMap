'''
Topic - Read and Write Files

# write to the file
with open("SkillStorm/Level6/users.txt", "w") as file:
    file.write("\n Bob Hope")

# open for reading
with open("SkillStorm/Level6/users.txt", "r") as file:
    for line in file:
        print(line)

print(file.closed)
'''

import csv

class User:

    row_number: int
    first: str
    last: str
    email: str
    
    def __init__(self, row_number, first, last, email) -> None:
        self.row_number = row_number
        self.first = first
        self.last = last
        self.email = email

class CSV_Parser:
    
    def parse_file(self, file_path):
        # store users in a list and return it
        user_list = []
        
        # open the csv file
        with open(file_path, "r") as file:
            
            # delimiter is the character that separates each column
            csv_reader = csv.reader(file, delimiter=",")
            
            # skip the headers with next() or a line counter
            next(csv_reader)
            
            line_count = 2
            
            for row in csv_reader:
                # csv module automatically puts each column into a list: [Dan,Pickles,dan.pickles@email.com]
                user = User(line_count, row[0], row[1], row[2])
                user_list.append(user)
                line_count += 1
        
        return user_list

users = CSV_Parser()
print(users.parse_file("SKillStorm/Level6/users.csv"))