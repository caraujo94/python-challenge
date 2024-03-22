#Import the required libraries

import os
import csv
from pathlib import Path


csvpath = os.path.join('../PyPoll/Resources/election_data.csv')

# Read csv file and calculate necessary information from file

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Total_votes = 0
    Charles_votes = 0
    Diana_votes = 0
    Raymon_votes = 0
    Other_votes = 0
    # Read each row of data after the header
    for row in csvreader:
        #find total votes
        Total_votes = Total_votes+1
        #conditional to determine votes by candidate
        if row[2] == 'Charles Casper Stockham':
            Charles_votes = Charles_votes + 1
        elif row[2] == 'Diana DeGette':
            Diana_votes = Diana_votes + 1
        elif row[2] == 'Raymon Anthony Doane':
            Raymon_votes = Raymon_votes + 1
        else:
            Other_votes = Other_votes + 1
        
        #calculated percentages of total
        Charles_pct = Charles_votes/Total_votes
        Diana_pct = Diana_votes/Total_votes
        Raymon_pct = Raymon_votes/Total_votes
    
        if Charles_votes > Diana_votes and Charles_votes > Raymon_votes:
            winner = "Charles Casper Stockham"
        elif Diana_votes > Charles_votes and Diana_votes > Raymon_votes:
            winner = "Diana DeGette"   
        else:
            winner = "Raymon Anthony Doane"
    
    #print requirements
    print("Election Results \n")
    print("---------------")
    print(f'Total Votes: {Total_votes}')
    print(f'Charles Casper Stockham: ' +  "{:.3%}".format(Charles_pct) + f' ({Charles_votes})')
    print(f'Diana DeGette: ' +  "{:.3%}".format(Diana_pct) + f' ({Diana_votes})')
    print(f'Raymon Anthony Doane: ' +  "{:.3%}".format(Raymon_pct) + f' ({Raymon_votes})')
    print("---------------")
    print(f'Winner: {winner}')
          
# Specify the file to write to
output_path = os.path.join('output', 'new.csv')     

          
     # Open the file using "write" mode. Specify the variable to hold the contents.  Had to add newline = '' to avoid skipped rows
with open(output_path, 'w', newline = '') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Votes', 'Charles Votes', 'Charles Percent','Diana Votes'
                        ,'Diana Percentage','Raymon Votes','Raymon Percentage','Winner'])

    # Write the second row
    csvwriter.writerow([Total_votes,Charles_votes,Charles_pct, Diana_votes, Diana_pct,Raymon_votes,Raymon_pct, winner])     
          
          