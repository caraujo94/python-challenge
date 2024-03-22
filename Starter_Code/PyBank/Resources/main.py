#PyBank

#Import the os module to create file paths

import os
import csv
from pathlib import Path

csvpath = os.path.join('../PyBank/Resources/budget_data.csv')

# Read csv file and calculate necessary information from file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #set variables
    Total_months = 0
    Total = 0
    Max_increase = 0
    Max_decrease = 0
    Max_increase_month = 0
    Max_decrease_month = 0
    Average_change = 0
    Previous_row = 0
    Difference = 0
    Cml_difference = 0


    # Read each row of data after the header
    for row in csvreader:
      
        #increment months
        Total_months = Total_months+1
        
        #calculate difference
        if Total_months > 1:
            Difference = int(row[1]) - Previous_row
        else:
            Difference = 0
        #calculate cumlative differences
        Cml_difference = Cml_difference + Difference
        
        #add up total
        Total = Total + int(row[1])
        #conditional to determine min and max
        if Difference < Max_decrease:
            Max_decrease =Difference
            Max_decrease_month = (row[0])
        else:
            Max_decrease = Max_decrease
        #conditional to determine min and max
        if Difference > Max_increase:
            Max_increase = Difference
            Max_increase_month = (row[0])
        else:
            Max_increase = Max_increase  
            
        #Set current value so next loop will reference it as the prior value        
        Previous_row = int(row[1])
        
    #calculate average change, n-1 as the first value has no change
    Average_difference = Cml_difference/(Total_months-1)
    
    #print requirements
    print(f"Financial Analysis \n---------------------")
    print(f"Total Months: {Total_months}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${Average_difference}")
    print(f"Greatest Increase in Profits: {Max_increase_month} (${Max_increase})")
    print(f"Greatest Decrease in Profits: {Max_decrease_month} (${Max_decrease})")
          
# Specify the file to write to
output_path = os.path.join('output', 'new.csv')     

          
     # Open the file using "write" mode. Specify the variable to hold the contents.  Had to add newline = '' to avoid skipped rows
with open(output_path, 'w', newline = '') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total Amount', 'Average Change','Greatest Increase Month'
                        ,'Greatest Increase','Greatest Decrease Month','Greatest Decrease'])

    # Write the second row
    csvwriter.writerow([Total_months,Total,Average_difference, Max_increase_month, Max_increase,Max_decrease_month,Max_decrease])     
          
          