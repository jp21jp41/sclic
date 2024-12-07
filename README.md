# sclic
An attempt at a command line alternative to "Point-and-Click-ETL".

Differences:
Whereas the first idea was to use a Graphical User Interface, the current solution is instead to use a Command Line Interface. A major advantage to using the command line (while at the expense of user experience) is efficiency. That means that there is never a window that pops up, though it is likely that if the user base is mostly those wanting to perform data analysis, they ought to have the ability to select data and the like with a bit of ease.
There are less selections, yet they are more broadened: one should be able to select "categories" and "data" and they are all only considered columns and are narrowed down later (such processes are to be implemented later). The idea is that such selections allow for looser data selection, meaning that one could see how two data columns are correlated, for instance.
There are plans for a vast number of tests to be at the user's disposal. That requires being very attentive to the specifications of the tests as well as the needs of the user; particularly, the dataset still has to be readable, so giving the user the ability to do a variety of different tests to have them all in one dataset is paramount.

The inability to sufficiently run the statistical tests is the biggest barrier to it. The narrow down process so far has a problem in which the columns and rows selected reset every time such that the selection cannot yet be nested (if I had a column of colors and a column of containers and I wanted "blue tupperware", I would only be able to select either all blue containers or all tupperware containers, not both). That with the lack of proper comparison methods unfortunately stops the project in its tracks.
