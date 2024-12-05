# sclic
An attempt at a command line alternative to "Point-and-Click-ETL".

Differences:
Whereas the first idea was to use a Graphical User Interface, the current solution is instead to use a Command Line Interface. A major advantage to using the command line (while at the expense of user experience) is efficiency. That means that there is never a window that pops up, though it is likely that if the user base is mostly those wanting to perform data analysis, they ought to have the ability to select data and the like with a bit of ease.
There are less selections, yet they are more broadened: one can select "categories" and "data" and they are all only considered columns and are narrowed down later (such processes are to be implemented later). The idea is that such selections allow for looser data selection, meaning that one could see how two data columns are correlated, for instance.
There are plans for a vast number of tests to be at the user's disposal. That requires being very attentive to the specifications of the tests as well as the needs of the user; particularly, the dataset still has to be readable, so giving the user the ability to do a variety of different tests to have them all in one dataset is paramount.
