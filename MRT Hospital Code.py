# This is my second project
# In this project, I want to build a simple CLI application that a hospital can use to create, edit and view patients' records.


# Import some modules that would be useful for the CLI app.

# The randint will be used to generate a random patient number everytime a new patient seeks treatment
from random import randint

# The datetime module will be used to track the time a patient has started treament while in the hospital
from datetime import datetime, date

# This is a list to store all the card numbers of each patient. It will be trasversed from time to time.
cards_num = []
