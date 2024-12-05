# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:04:11 2024

@author: justi
"""

# Import libraries
import pandas as pnd
import scipy
import numpy
import math
import sys


"""
Function to take input values and give them potential
outting processes
- opt: the type of opt that the user would take
-- opt = 'out': opting out of the program, meaning the user
would be using 'sys.exit()'
-- opt = 'backtrack': opting to backtrack out of the given input
(not yet implemented)
"""
def inputter(opt = 'out'):
    ipt = input()
    if ipt == '':
        if opt == 'out':
            print('Are you trying to opt-out of the program?')
            print('Type "Yes" if so.')
            yn_check = 0
            yn = input()
            while yn_check == 0:
                if yn == 'Yes':
                    print('Are you sure?')
                    print('Yes/No')
                    opt_check = 0
                    while opt_check == 0:
                        opt = input()
                        if opt == 'Yes':
                            print('Opting out')
                            sys.exit()
                        elif opt == 'No':
                            print('Continuing with the program using an empty space')
                            opt_check += 1
                            yn_check += 1
                else:
                    print('Continuing with the program using an empty space')
                    yn_check += 1
        
        if opt == 'backtrack':
            print('Are you trying to backtrack?')
            print('Type "Yes" if so.')
            yn_check = 0
            yn = input()
            while yn_check == 0:
                if yn == 'Yes':
                    print('Are you sure?')
                    print('Yes/No')
                    opt_check = 0
                    while opt_check == 0:
                        opt = input()
                        if opt == 'Yes':
                            print('Backtracking')
                            return 'empty_backtrack'
                        elif opt == 'No':
                            print('Continuing with the program using an empty space')
                            opt_check += 1
                            yn_check += 1
                else:
                    print('Continuing with the program using an empty space')
                    yn_check += 1
    return(ipt)

class Converter:
    def __init__(self, name):
        self.name = name
        self.data = {}
        self.categoricals = []
        self.raw_name = str(name)
        self.data_columns = {}
        self.categorical_columns = {}
        
    
    def ask(self, question, choices = ['Yes', 'No'], 
            results = [0, 1], lister = 'options', 
            outputter = ['N/A'], result_opt = 0):
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
            yn = inputter('backtrack')
            # Try statement to put a choice that
            # corresponds with a result
            try:
                q_ans = results[choices.index(yn)]
                ask_ans += 1
            # Exception to retry the loop
            except:
                print('Answer not read\n')
                return
        # Return the resulting function if the lister
        # is set to 'functions'
        for output in outputter:
            if outputter == 'functions':
                try:
                    exec(str(self.raw_name) + '.' +  str(q_ans))
                except:
                    pass
        # Return the answer result
        else:
            return(q_ans)


    # A function to read the directory of a given dataset.
    def data_read(self):
        # Directory selection with nested try-exceptions
        dir_check = 0
        while dir_check == 0:
            print('Please enter the directory:')
            directory = inputter()
            try:
                dataset = pnd.read_csv(directory)
                dir_check += 1
            except:
                try:
                    dataset = pnd.read_table(directory)
                    dir_check += 1
                except:
                    try:
                        dataset = pnd.read_excel(directory)
                        dir_check += 1
                    except:
                        print('File not read.')
                        dir_check = self.ask('Do you want to attempt to read again?', ["Yes", "No"], [0, 1])
        self.dataset = dataset
        self.row_numbers = list(dataset.index)
        
    
    
    
    def row_narrower(self, col_parsed, nar_cont = 0):
        self.col_unique_values = list(self.dataset[col_parsed].unique())
        print('Here are all of the choices for the given column:')
        print(self.col_unique_values)
        col_choice = self.ask('Select the given column choice:', self.col_unique_values, self.col_unique_values, 'raw')
        if nar_cont == 0:
            self.remaining_categoricals = [self.categorical_columns[col_parsed] == col_choice]
            self.remaining_data = self.dataset[self.categorical_columns[col_parsed] == col_choice]
            print('Here are all of the remaining data options:')
            print(self.remaining_data)
        elif nar_cont == 1:
            self.remaining_categoricals.append([self.categorical_columns[col_parsed] == col_choice])
            self.remaining_data = pnd.concat([self.remaining_data, self.categorical_columns[col_parsed] == col_choice])
            print('Here are all of the remaining data options:')
            print(self.remaining_data)
        nar_cont = self.ask('Would you like to select another categorical column?', ['Yes', 'No'], [1, 0])
        if nar_cont == 1:
            return self.row_narrower(col_parsed, nar_cont)
        
    """
    Function to append a chosen column
    """
    def column_appender(self, set_type):
        if set_type == 'categorical':
            set_str = 'categories'
        else:
            set_str = set_type
        column_choice = self.ask('Add a column to inspect ' + set_str + ' from', self.column_values, self.column_values, 'raw', result_opt = '')
        if column_choice in self.column_values:
            exec(str(self.raw_name) + '.' + str(set_type) + '_columns.update({column_choice : ' + str(self.raw_name) + '.dataset["' + str(column_choice) + '"]})')
            self.column_values.remove(column_choice)
        else:
            print('Column not found')
        return self.ask('Do you want to add another column?', results = [['column_appender(set_type)', 0], ['Continue', 1]], lister = 'raw', outputter = 'functions')[1]
        


    """
    Function to select data columns
    """
    def column_splay(self):
        self.column_values = []
        check_value = 0
        self.selected_columns = {}
        for column in self.dataset.columns:
            self.column_values.append(column)
        while check_value == 0 and len(self.column_values) > 0:
            check_value = self.column_appender('data')
        self.data = pnd.DataFrame(self.selected_columns)
        
    
    """
    Function to ask user for opt out or selection
    of categorical columns
    """
    def column_specifier(self):
        spec_check = 0
        while spec_check == 0:
            spec_check = self.column_appender('categorical')
            """
            value = self.ask('Would you like to select columns to classify rows?')
            if value == 0:
                spec_check = self.column_appender('categorical')
            elif value == 0:
                spec_check += 1
            else:
                print('Answer not read \n')
                """


    """
    Function to select categorical columns
    """
    def choose_columns(self):
        spec_check = 0
        selected_columns = {}
        while spec_check == 0:
            print('Here are the selectable columns:')
            print(self.column_values)
            print('Select a new column:')
            column_choice = inputter()
            spec_check = self.column_appender(column_choice, selected_columns, spec_check)
        return selected_columns
            
    """
    Function to select statistical operations
    """
    def statistical_selector(self):
        cat_values = []
        self.cats_adj = {}
        stat_ops = ['T-test', 'ANOVA', 'MANOVA', 'Convert Data', 'Time Series',
                    'Odds Ratio', 'Prevalence', 'Wald Test']
        stat_choice = self.ask('What type of statistical operation would you like to make?', stat_ops, stat_ops)
        if stat_choice == 'T-test':
            cat_columns = []
            for category in self.categorical_columns:
                # Possibly deleted 'cat_columns'
                cat_columns.append(category)
                self.cats_adj.update({category : self.categorical_columns[category]})
            choice_ender = 0
            while choice_ender == 0:
                choice_selector = self.ask('Would you like to select for proportions or means?', ['Proportions', 'Means'], [0, 1])
                if choice_selector == 0:
                    print('Proportions not yet constructable.')
                elif choice_selector == 1:
                    col_selector = self.ask('Would you like to select categorical columns or skip?', ['Categorical', 'Skip'], [0, 1])
                    while col_selector == 0:
                        col_parsed = self.ask('Select a column to parse:', cat_columns, cat_columns, 'raw')
                        # Needs to be fixed
                        self.row_narrower(col_parsed)
                        
                        col_selector = self.ask('Do you want to add another column?', ['Yes', 'No'], [0, 1])
                        
                        
                choice_ender = self.ask('Would you like to continue?', ['Yes', 'No'], [0, 1])
                
    
# Create converter function
dt_cvt = Converter('dt_cvt')

# Read data
dt_cvt.data_read()

# Create data columns
dt_cvt.column_splay()

dt_cvt.column_specifier()    

dt_cvt.statistical_selector()


