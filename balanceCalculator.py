# Project:      Lab 3 (HagensPianoLab03redo.py)
# Name:         Piano Hagens
# Date:         09/15/2017
# Description:  #ProgramsB will calculate how much need to save per month in order to reach $1,125,000 at age 68.           

# ProgramsB will calculate how much need to save per month in order to reach $1,125,000 at age 68.
def mainB():
    print("------------- Lab 3 B calculate target saving------------- ")
    print()
    # Enter balance of your savings account
    fltBankBalance = float(input("Enter balance of your savings account: "))
                           
    # Enter your age
    intAgeYear = int(input("Enter a number of your age: "))
    input()
                     
    # Calculate the YearSaving = (1,125,000 - CurrentSaving) / CurentAge
    YearSaving = (1125000 - fltBankBalance) / intAgeYear
                     
    # Calculate the monthlySaving = YearSaving / 12
    monthlySaving = YearSaving / 12
    print("---------------------------------------------------")
    
    # Display the result
    # YearSaving
    print("From now on you need to save: ", YearSaving, "dollars to reach 1,125,000 on your age of 68 per year")
    
    # monthlySaving 
    print("From now on you need to save: ", monthlySaving, "dollars to reach 1,125,000 on your age of 68 per Month")
    
# Call mainB funtion
mainB()
