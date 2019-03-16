# Author: Jeff Mitchell
# Date: 17 March 2019
# Version: 0.2
# Quick Desc: Program to convert expenses into Annual, Monthly, Fortnightly and
# Weekly

# To be fixed:

# Future capability:
# Subtract an expense from total

# set initial values for totals
total_weekly, total_fortnightly, total_monthly, total_annually = 0, 0, 0, 0
start_frequency = 0
start_amount = 0


def convert_fortnightly(annually):
    local_fortnightly = annually / 26
    return local_fortnightly


def convert_monthly(annually):
    local_monthly = annually / 12
    return local_monthly
	

# convert annual expenses into weekly, fortnightly and monthly amounts
def convert_weekly(annually):
    local_weekly = annually / 52
    return local_weekly


# display converted amounts
def display_converted_amounts(weekly, fortnightly, monthly, annually):
    print("\nA starting amount of ${:.2f} converts as follows:" .format(start_amount))
    print("\nWeekly it is: ${:.2f}" .format(weekly))
    print("Fortnightly it is: ${:.2f}" .format(fortnightly))
    print("Monthly it is: ${:.2f}" .format(monthly))
    print("Annually it is: ${:.2f}" .format(annually))


# display total amounts
def display_total_amounts(weekly, fortnightly, monthly, annually):
    print("\nTotal weekly expenses are: ${:.2f}" .format(weekly))
    print("Total fortnightly expenses are: ${:.2f}" .format(fortnightly))
    print("Total monthly expenses are: ${:.2f}" .format(monthly))
    print("Total annual expenses are: ${:.2f}" .format(annually))
	
	
# convert fortnightly into annual expense
def fortnightly_to_annual(fortnightly):
    local_annual = fortnightly * 26
    return local_annual


# make calculations by calling functions based on frequency.
# expenses are converted to an annual amount
# annual amount is then converted into the other three categories and returned
def frequency_conversion(frequency, start_amount):
    if frequency == 1:
        local_annual = weekly_to_annual(start_amount)
    elif frequency == 2:
        local_annual = fortnightly_to_annual(start_amount)
    elif frequency == 3:
        local_annual = monthly_to_annual(start_amount)
    else:
        local_annual = start_amount
    return local_annual


# get and assign starting amount from user
def get_start_amount():
    while True:
        try:
            local_start_amount = float(input("\nWhat is your starting amount? "))
        except ValueError:
            print("\nSorry that is not a valid starting amount. Please enter a number.")
            continue
        else:
            break
    return local_start_amount


def main():
    repeat = True
    low = 1
    high = 5
    while repeat:
        try_again = False
        main_message()
        try:
            action = int(input('\nPlease enter the number for your '
                               'selection --> '))
        except ValueError:
            print('Please enter a number between {} and {}.'.format(low, high))
            try_again = True
        else:
            if action < low or action > high:
                print('\nPlease select from the available options ({} - {})'
                      .format(low, high))
                try_again = True
            elif action == low:
                help_menu()
            elif action == 2:
                start_frequency = user_frequency() # get frequency
    			start_amount = get_start_amount() #get starting amountto be converted
    			annually = frequency_conversion(start_frequency, start_amount) # identify annual total from freqeuncy conversion
    			weekly = convert_weekly(annually)
    			fortnightly = convert_fortnightly(annually)
    			monthly = convert_monthly(annually)
    			# update total amounts
    			total_weekly += weekly
    			total_fortnightly += fortnightly
    			total_monthly += monthly
    			total_annually += annually
    			# function call to display converted amounts
    			display_converted_amounts(weekly, fortnightly, monthly, annually)
    			# function call to display total amounts 
    			display_total_amounts(total_weekly, total_fortnightly, total_monthly, total_annually)
    			repeat = user_repeat()
    			if repeat == "n":
    				selection = 4
            elif action == 3:
                display_total_amounts(total_weekly, total_fortnightly, total_monthly, total_annually)
            elif action == 4:
                correct_input = False
    			while correct_input == False:
    				confirm_reset = input("\nAre you sure that yuo want to reset the totals? (y/n): ")
    				confirm_reset = confirm_reset.lower()
    				if confirm_reset != "y" and confirm_reset != "n":
    					print("\nSorry, that is not a valid selection. Please either 'y' or 'n'.")
    				elif confirm_reset == "n":
    					correct_input = True
    				else:
    					total_weekly, total_fortnightly, total_monthly, total_annually = reset_totals()
    					print("\nAll totals have been reset")
    					correct_input = True
            elif action == high:
                print('\nIf you have generated any files, please find them '
                      'saved to disk. Goodbye.')
                sys.exit()
            if not try_again:
                repeat = ad.check_repeat()
        print('\nPlease find your files saved to disk. Goodbye.')


def main_message():
    """Display menu of options."""
    print('\n\n*************==========================*****************')
    print('\nConver Expenses version 0.11')
    print('Created by Jeff Mitchell, 2019')
    print('\nOptions:')
    print('\n1. Help Menu')
    print('2. Convert an expense')
    print('3. Show current expense totals')
    print('4. Reset the current expense totals')
    print('5. Exit')


# convert monthly into annual expense
def monthly_to_annual(monthly):
    local_annual = monthly * 12
    return local_annual


# reset totals to zero
def reset_totals():
    local_weekly = 0
    local_fortnightly = 0
    local_monthly = 0
    local_annual = 0
    return local_weekly, local_fortnightly, local_monthly, local_annual


# get and assign frequency selected by user
def user_frequency():
    print("""\nPlease enter a number to select a frequency for the expense from the following:\n
1. Weekly
2. Fortnightly
3. Monthly
4. Annual\n""")
    correct_input = False
    while correct_input == False:
        local_frequency = int(input("Please type a number between 1 and 4 for the frequency of the expense: "))
        if local_frequency > 0 and local_frequency < 5:
            correct_input = True
        else:
            print("\nThat is not a valid option. Please enter a number between 1 and 4.\n")
    return local_frequency


# see if user wishes to repeat
def user_repeat():
    # y/n and check if neither selected
    local_repeat = input("\nDo you want to continue with another amount or selection? (y/n): ")
    local_repeat = local_repeat.lower()
    if local_repeat != "y" and local_repeat != "n":
        print("\nSorry, that is not a valid selection. Please either 'y' or 'n'.")
        local_repeat = user_repeat()        
    return local_repeat
	
	
# get user selection
def user_selection():
    correct_input = False
    while correct_input == False:
        while True:
            try:
                local_selection = int(input("Please make a selection: "))
            except ValueError:
                print("\nSorry, that is not a valid selection. Please enter a number between 1 and 4.\n")
                continue
            else:
                break

        if local_selection > 0 and local_selection < 5:
            correct_input = True
        else:
            print("\nYou must enter a number betweeen 1 and 4\n")
        
    # return selection
    return local_selection


# convert weekly into annual expense
def weekly_to_annual(weekly):
    local_annual = weekly * 52
    return local_annual
	
	
if __name__ == '__main__':
    main()        
