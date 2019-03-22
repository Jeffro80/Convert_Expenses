# Convert Expenses

Convert Expenses converts expenses to weekly, fortnightly, monthly and annual figures.
It totals these expenses to provide figures for a weekly, fortnightly, monthly and annual
budget.

## Version

Version Number 0.1  

App last updated 17 March 2019  
Readme last updated 22 March 2019

## Operation

Run Convert_Expenses.py from within Spyder etc.

## Functions

- Convert an expense into weekly, fortnightly, monthly and annual amounts
- Show current expense totals

## Dependencies

The following third-party libraries are imported and therefore are required for
the app to run:

- admintools from the custtools library

## Development

### Known bugs

- Nill

### Current development step

- Refactoring of code to improve

### Required development steps

- Update docstrings
- Move functions out of main() into separate functions
- Place totals etc into a dictionary that can be passed around functions
- Refactor functions to receive the totals dict and to update the dict before returning it
- Move calculation steps in functions to the return line (rather than returning the variable)
- Shorten line lengths so within spec
- Update help menu with helper function calls
- Add helper functions
- Update help_menu_message() with help function descriptions

### Future additions

- Subtract an expense from total

## License
The content of this repository is licensed under a [Creative Commons Attribution License](http://creativecommons.org/licenses/by/3.0/us/)