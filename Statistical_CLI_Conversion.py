# -*- coding: utf-8 -*-
"""
Statistical CLI Conversion
Justin Pizano
"""

import pandas as pnd



# A dictionary of the functions with their parameters
function_snapshots = {}

"""
Function to ask questions with two distinct
responses throughout input processes
- question: the question asked
- choice1: the first choice
- choice2: the second choice
"""
def ask(question, choice1, choice2):
    # incrementable variables
    ask_ans = 0
    q_ans = 0
    # While-loop to ask the question
    while ask_ans == 0:
        print(question)
        print(choice1 + '/' + choice2)
        # Inputting the choice
        yn = input()
        # If the answer is choice1, the outer loop
        # continues
        if yn == choice1:
            ask_ans += 1
        # If the answer is choice2, other outer loop
        # processes inevitably follow through
        elif yn == choice2:
            ask_ans += 1
            q_ans += 1
        # If the answer is neither choice1 nor choice2,
        # the inner loop continues
        else:
            print('Answer not read\n')
    # Return the resulting answer choice number
    # (0 if choice1, 1 if choice2)
    return(q_ans)




# A function to read the directory of a given dataset.
def data_read():
    # Directory selection with nested try-exceptions
    print('Please enter the directory:')
    directory = input()
    dir_check = 0
    while dir_check == 0:
        try:
            data_set = pnd.read_csv(directory)
            dir_check += 1
        except:
            try:
                data_set = pnd.read_table(directory)
                dir_check += 1
            except:
                try:
                    data_set = pnd.read_excel(directory)
                    dir_check += 1
                except:
                    print('File not read.')
                    dir_check = ask('Do you want to attempt to read again?', "Yes", "No")
                    data_set = pnd.DataFrame({})
    
    return data_set


"""
Function to append a chosen column
"""
def column_appender(column_choice, column_values, selected_columns, check_value):
    if column_choice in column_values:
        selected_columns.append(x[column_choice])
        column_values.remove(column_choice)
        check_value = ask('Do you want to add another column?', "Yes", "No")
    else:
        print('Column not found')
    return check_value



"""
Function to select data columns
"""
def column_splay(column_values):
    check_value = 0
    selected_columns = []
    for column in x.columns:
        column_values.append(column)
    while check_value == 0 and len(column_values) > 0:
        print('Here are the selectable columns:')
        print(column_values)
        print('Add a column')
        print('to inspect data from:')
        column_choice = input()
        check_value = column_appender(column_choice, column_values, selected_columns, check_value)
    return selected_columns
    
  
"""
Function to ask user for opt out or selection
of categorical columns
"""
def column_specifier(column_values):
    spec_check = 0
    while spec_check == 0:
        print('Would you like to select columns to classify rows?')
        print('Yes/No')
        value = input()
        if value == 'Yes':
            specified_columns = choose_columns(column_values)
            return specified_columns
        elif value == 'No':
            spec_check += 1
        else:
            print('Answer not read \n')
    return []


"""
Function to select categorical columns
"""
def choose_columns(column_values):
    spec_check = 0
    selected_columns = []
    while spec_check == 0:
        print('Here are the selectable columns:')
        print(column_values)
        print('Select a new column:')
        column_choice = input()
        spec_check = column_appender(column_choice, column_values, selected_columns, spec_check)
    return selected_columns
        
"""
Function to select statistical operations
"""
def statistical_selector(data, categoricals, rows):
    cat_values = []
    print('What type of statistical operations would you like to make?')
    print('Here are the options (Note: the default is "t-tests"):')
    print('|\t"T-test"\t|\t"ANOVA"\t|\t"MANOVA"\t|\t"Convert Data"\t|\t"Time Series\t|')
    print('\t|\t"Odds Ratio"\t|\t"Prevalence\t|\t"Wald Test"\t|\t"')
    choice = input()
    if choice == 'T-test':
        print('T-test test')


# Read data and print dataset
x = data_read()
print(x)

# Instantiate column values
column_values = []

# Create data columns
data_columns = column_splay(column_values)

# Create (or opt out of) categorical columns
categorical_columns = column_specifier(column_values)

# Run statistical operations
statistical_selector(data_columns, categorical_columns, data_columns[0])


