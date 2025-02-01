# -*- coding: utf-8 -*-
"""
Statistical CLI Conversion
Justin Pizano
"""

import pandas as pnd
import scipy
import numpy
import math
            

# A dictionary of the functions with their parameters
function_snapshots = {}

"""
Function to ask questions with two distinct
responses throughout input processes
- question: the question asked
- choices: the list of choices
- results: the list of results
- lister: how the list of choices is printed
(with only 'options' and 'raw' for now)
"""
def ask(question, choices, results, lister = 'options'):
    # Incrementable variables
    ask_ans = 0
    # While-loop to ask the question
    while ask_ans == 0:
        print(question)
        if lister == 'options':
            ch_str = ''
            for choice in choices:
                if choices.index(choice) == len(choices) - 1:
                    ch_str += choice
                else:
                    ch_str += choice + ' / '
        elif lister == 'raw':
            ch_str = str(choices)
        print(ch_str)
        # Inputting the choice
        yn = input()
        # Try statement to put a choice that
        # corresponds with a result
        try:
            q_ans = results[choices.index(yn)]
            ask_ans += 1
        # Exception to retry the loop
        except:
            print('Answer not read\n')
    # Return the answer result
    return(q_ans)


def row_narrower(categoricals, data, col_parsed):
    col_unique_values = list(categoricals[col_parsed].unique())
    print('Here are all of the choices for the given column:')
    print(col_unique_values)
    col_choice = ask('Select the given column choice:', col_unique_values, col_unique_values, 'raw')
    remaining_categoricals = [categoricals[col_parsed] == col_choice]
    print('Here are all of the remaining data options:')
    remaining_data = data[categoricals[col_parsed] == col_choice]
    print(remaining_data)
    nar_cont = ask('Would you like to select another categorical column?', ['Yes', 'No'], [0, 1])
    if nar_cont == 0:
        return row_narrower(categoricals, data, )


def stat_test(rows, test_type):
    print('test')




# A function to read the directory of a given dataset.
def data_read():
    # Directory selection with nested try-exceptions
    dir_check = 0
    while dir_check == 0:
        print('Please enter the directory:')
        directory = input()
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
                    dir_check = ask('Do you want to attempt to read again?', ["Yes", "No"], [0, 1])
                    data_set = pnd.DataFrame({})
    
    return data_set


"""
Function to append a chosen column
"""
def column_appender(column_choice, column_values, selected_columns, check_value):
    if column_choice in column_values:
        selected_columns.update({column_choice : x[column_choice]})
        column_values.remove(column_choice)
    else:
        print('Column not found')
    check_value = ask('Do you want to add another column?', ["Yes", "No"], [0, 1])
    return check_value



"""
Function to select data columns
"""
def column_splay(column_values, data_set):
    check_value = 0
    selected_columns = {}
    for column in data_set.columns:
        column_values.append(column)
    while check_value == 0 and len(column_values) > 0:
        column_choice = ask('Add a column to inspect data from', column_values, column_values, 'raw')
        check_value = column_appender(column_choice, column_values, selected_columns, check_value)
    return pnd.DataFrame(selected_columns)
    
  
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
    selected_columns = {}
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
    stat_ops = ['T-test', 'ANOVA', 'MANOVA', 'Convert Data', 'Time Series',
                'Odds Ratio', 'Prevalence', 'Wald Test']
    stat_choice = ask('What type of statistical operation would you like to make?', stat_ops, stat_ops)
    if stat_choice == 'T-test':
        cat_columns = []
        for category in categoricals:
            cat_columns.append(category)
        choice_ender = 0
        while choice_ender == 0:
            choice_selector = ask('Would you like to select for proportions or means?', ['Proportions', 'Means'], [0, 1])
            if choice_selector == 0:
                print('Proportions not yet constructable.')
            elif choice_selector == 1:
                col_selector = ask('Would you like to select categorical columns or skip?', ['Categorical', 'Skip'], [0, 1])
                while col_selector == 0:
                    col_parsed = ask('Select a column to parse:', cat_columns, cat_columns, 'raw')
                    row_narrower(col_parsed, rows)

                    
                    col_selector = ask('Do you want to add another column?', ['Yes', 'No'], [0, 1])
                    
                    
            choice_ender = ask('Would you like to continue?', ['Yes', 'No'], [0, 1])
        


# Read data and print dataset
x = data_read()
print(x)

# Instantiate column values
column_values = []

# Create data columns
data_columns = column_splay(column_values, x)

# Create (or opt out of) categorical columns
categorical_columns = column_specifier(column_values)

# Run statistical operations
statistical_selector(data_columns, categorical_columns, list(x).index)


