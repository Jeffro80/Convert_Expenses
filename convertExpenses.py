# Author: Jeff Mitchell
# Date: 17 March 2019
# Version: 0.2
# Quick Desc: Program to convert expenses into Annual, Monthly, Fortnightly and
# Weekly

# To be fixed:

# Future capability:
# Subtract an expense from total


import copy
import custtools.admintools as ad
import sys


def convert_expense(totals_dict):
    """Convert an expense into cost per period.
    
    Converts a supplied expense into the cost per period and updates the
    totals_dict with totals based on these costs. Also displays the results
    from this conversion.
    
    Args:
        totals_dict (dict): Dict holding the current totals value for each
        period.
        
    Returns:
        updated_totals (dict): Dict with the updated totals for each value.
    """
    updated_totals = copy.deepcopy(totals_dict)
    updated_totals['amount'] = get_amount()
    updated_totals['frequency'] = get_frequency()
    amount = updated_totals['amount']
    frequency = updated_totals['frequency']
    if frequency != 'annually':
        # Set amount to an annual amount
        amount = convert_to_annual(amount, frequency)
    # Convert amount to each frequency
    totals_list = []
    totals_list.append(updated_totals['amount'])
    totals_list.append(frequency)
    totals_list.append(convert_to_weekly(amount))
    totals_list.append(convert_to_fortnigthly(amount))
    totals_list.append(convert_to_monthly(amount))
    totals_list.append(amount)
    # Update totals_dict
    updated_totals['total_weekly'] += totals_list[2]
    updated_totals['total_fortnightly'] += totals_list[3]
    updated_totals['total_monthly'] += totals_list[4]
    updated_totals['total_annually'] += totals_list[5]
    # Display converted values for this amount and frequency    
    display_converted_amounts(totals_list)
    return updated_totals    


def convert_fortnightly(annually):
    """Convert annual amount to fortnightly cost.
    
    Args:
        annually (float): Annual cost.
        
    Returns:
        (float): Fortnightly cost.
    """
    return annually / 26


def convert_monthly(annually):
    """Convert annual amount to monthly cost.
    
    Args:
        annually (float): Annual cost.
        
    Returns:
        (float): Monthly cost.
    """
    return annually / 12
	

def convert_weekly(annually):
    """Convert annual amount to weekly cost.
    
    Args:
        annually (float): Annual cost.
        
    Returns:
        (float): Weekly cost.
    """
    return annually / 52


def display_converted_amounts(totals_list):
    """Display conversion amounts per frequency for a total.
    
    Args:
        totals_list (list): List with amount, frequency and totals starting
        with weekly.
    """
    print('\nA starting amount of ${:.2f} ({:.2f}) converts as follows: '
          .format(totals_list[0], totals_list[1]))
    print('\nWeekly it is: ${:.2f}'.format(totals_list[2]))
    print('Fortnightly it is: ${:.2f}'.format(totals_list[3]))
    print('Monthly it is: ${:.2f}'.format(totals_list[4]))
    print('Annually it is: ${:.2f}'.format(totals_list[5]))


def display_total_amounts(totals_dict):
    """Display the total expenses for each period.
    
    Args:
        totals_dict (dict): Dict with totals by frequency.
    """
    print('\nTotal weekly expenses are: ${:.2f}'.format(
            totals_dict['total_weekly']))
    print('Total fortnightly expenses are: ${:.2f}'.format(
            totals_dict['total_fortnightly']))
    print('Total monthly expenses are: ${:.2f}'.format(
            totals_dict['total_monthly']))
    print('Total annual expenses are: ${:.2f}'.format(
            totals_dict['total_annually']))
	
	
def fortnightly_to_annual(fortnightly):
    """Convert fortnightly amount to annual cost.
    
    Args:
        fortnightly (float): Fortnightly cost.
        
    Returns:
        (float): Annual cost.
    """
    return fortnightly * 26


def frequency_conversion(frequency, amount):
    """Convert a start amount to an annual amount.
    
    Annual amount calculated according to the frequency of the amount.
    
    Args:
        frequency (str): Frequency of payments.
        amount (float): Expense amount per frequency period.
    
    Returns:
        (float): Annual expense amount.
    """
    if frequency == 'weekly':
        return weekly_to_annual(amount)
    elif frequency == 'fortnightly':
        return fortnightly_to_annual(amount)
    elif frequency == 'monthly':
        return monthly_to_annual(amount)
    else:
        return amount


def get_amount():
    """Get expense amount from user.
    
    Get the expense amount from user and return as a float.
    
    Returns:
        amount (float): Amount of expense.
    """
    while True:
        try:
            amount = float(input('\nWhat is your starting amount? '))
        except ValueError:
            print('\nSorry that is not a valid starting amount. Please enter '
                  'a number.')
            continue
        else:
            break
    return amount


def get_frequency():
    """Get frequency of expense from user.
    
    Get the frequency of expense from user and return as a string.
    
    Returns:
        frequency (str): Frequency of expense.
    """
    frequencies = ['weekly', 'fortnightly', 'monthly', 'annually']
    print('\nPlease enter a number to select frequency of the expense:\n')
    print('1. Weekly')
    print('2. Fortnightly')
    print('3. Monthly')
    print('4. Annually\n')
    correct_input = False
    while not correct_input:
        frequency = int(input('Please type a number between 1 and 4 for the '
                              'frequency of the expense: '))
        if frequency > 0 and frequency < 5:
            correct_input = True
        else:
            print('\nThat is not a valid option. Please enter a number '
                  'between 1 and 4.\n')
    return frequencies[frequency-1]


def help_menu():
    """Display the requested help information."""
    repeat = True
    low = 1
    high = 4
    while repeat:
        try_again = False
        help_menu_message()
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
                pass # To Be Written
            elif action == 2:
                pass # To Be Written
            elif action == 3:
                pass # To Be Written
            elif action == high:
                repeat = False
        if not try_again:
            repeat = ad.check_repeat_help()


def help_menu_message():
    """Display the help menu options."""
    print('\nPlease enter the number for the item you would like help on:\n')
    print('1: <TBC>')
    print('2: <TBC>')
    print('3: <TBC>')
    print('4: Exit Help Menu')


def initialise_values():
    """Create dictionary to hold variables and initialise.
    
    Creates a dictionary that will hold the variables and initialises these
    variables. Totals are set to 0 and start_amount and start_frequency are
    provided by the user.
    
    Returns:
        totals_dict (dict): Totals for user variables.
    """
    start = 0
    totals_dict = {'total_weekly': start, 'total_fortnightly': start,
                   'total_monthly': start, 'total_annually': start}
    totals_dict['frequency'] = ''
    totals_dict['amount'] = 0
    return totals_dict


def main():
    # Create dictionary for values and initialise to 0
    totals_dict = initialise_values()
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
                totals_dict = convert_expense(totals_dict)
            elif action == 3:
                display_total_amounts(totals_dict)
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
    """Convert monthly amount to annual cost.
    
    Args:
        monthly (float): Monthly cost.
        
    Returns:
        (float): Annual cost.
    """
    return monthly * 12


# reset totals to zero
def reset_totals():
    local_weekly = 0
    local_fortnightly = 0
    local_monthly = 0
    local_annual = 0
    return local_weekly, local_fortnightly, local_monthly, local_annual





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


def weekly_to_annual(weekly):
    """Convert weekly amount to annual cost.
    
    Args:
        weekly (float): Weekly cost.
        
    Returns:
        (float): Annual cost.
    """
    return weekly * 52
	
	
if __name__ == '__main__':
    main()        
