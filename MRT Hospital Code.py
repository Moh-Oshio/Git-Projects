# This is my second project
# In this project, I want to build a simple CLI application that a hospital can use to create, edit and view patients' records.


# Import some modules that would be useful for the CLI app.

# The randint will be used to generate a random patient number everytime a new patient seeks treatment
from random import randint

# The datetime module will be used to track the time a patient has started treament while in the hospital
from datetime import datetime, date

# The os module is also needed to rename folders and files.
import os

# This is a list to store all the card numbers of each patient. It will be trasversed from time to time.
cards_num = []

# Now, it's time to start defining classes.
# Firstly, we have the Reception section. This is the first section the patient encounters upon entering the hospital.
# - In the case of a new patient, the Reception is tasked with collecting contact info, age and other important information. The Recption is also expected to take the card to the doctor who then instructs the nurses what to do.
# - In the case of an old patient, the patient submits their hospital card and the nurses get the hospital file of such patient and then hands the hospital file to the doctor who then calls the patient in for examination.


class Reception:
    def __init__(self):
        # there should be a try - except block at this point to catch erroneous hospital numbers.
        # This block checks if the provided card number is not in the folder. If it is but it is not in the folder, the number gets appended to the cards_num list. Else, it passes.
        try:
            with open('file_numbers.txt', 'r') as file:
                for line in file:
                    number = line.strip()
                    if number and number not in cards_num:
                        cards_num.append(number)
        except FileNotFoundError:
            pass

        self.folder = "patients"

        os.makedirs(self.folder, exist_ok=True)

    # Another class is created to generate ranodm patient numbers between 100 and 5000
    def num_gen(self):
        rand_num = str(randint(100, 5000))

        def_len = 6

        new_num = (((def_len - len(rand_num)) * '0') + rand_num)

        cards_num.append(new_num)

        with open('file_numbers.txt', 'a') as file:
            file.write(f'{new_num}\n')

        return new_num

    # ANother class to create a card for a new patient. This card should contain the patient's details such as age, address, and phone number.
    def create_card(self):
        file_no = cards_num[-1]

        name = input("Enter patient's name: \n\n").upper()

        sex = input("\nMale or Female? \n\n").title()

        dob = input("\nEnter date of birth in the format: dd/mm/yyyy \n\n")

        dob_date = datetime.strptime(dob, "%d/%m/%Y").date()

        today = date.today()

        age = today.year - dob_date.year

        if (today.month, today.day) < (dob_date.month, dob_date.day):
            age -= 1

        address = input("\nEnter address: \n\n")

        phone_number = input("\nEnter phone number: \n\n")

        file_path = os.path.join(self.folder, f'{file_no}.txt')

        with open(file_path, 'a') as file:
            file.write(
                f"--- PATIENT CARD CREATED ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})  ---\n")

            file.write(f'File Number: {file_no}\n')

            file.write(f'Name of Patient: {name}\n')

            file.write(f'Sex: {sex}\n')

            file.write(f'Age: {age}\n')

            file.write(f'Address: {address}\n')

            file.write(f'Phone: {phone_number}\n')

    def check_patient_file(self, card_number):
        file_path = os.path.join(self.folder, f"{card_number}.txt")

        if os.path.exists(file_path):
            print(f"\n---- Patient Record ({card_number}) ----\n")
            with open(file_path, 'r') as file:
                print(file.read())
            print("------------------------\n")
            return True
        else:
            print(f"\nPatient file does not exist.\n")
            return False

    def vital_signs(self, card_no):
        file_path = os.path.join(self.folder, f"{card_no}.txt")

        if not os.path.exists(file_path):
            print("\nPatient file not found.")
            return

        print("\nEnter vital signs:\n")
        temp = input("Temperature (°C): ")
        bp = input("Blood Pressure (mmHg): ")
        pulse = input("Pulse (bpm): ")

        with open(file_path, 'a') as file:
            file.write(
                f"\n--- VITAL SIGNS ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f"Temperature: {temp}°C\n")
            file.write(f"Blood Pressure: {bp}mmHg\n")
            file.write(f"Pulse: {pulse} bpm\n")

        print("\nVital signs recorded successfully!\n")

    def all_records(self):
        return cards_num


class Doctor:

    folder = patients

    def enter_report(self, card_no):
        file_path = os.path.join(self.folder, f"{card_no}.txt")

        if not os.path.exists(file_path):
            # checks for a patient card using the card no
            print("\nPatient file not found")
            return

        # If there is a patient card with the specified card number, the doctor's diagnosis, prescription and additional notes should be entered.
        print("\nEnter doctor's report:\n")
        diagnosis = input("Diagnosis: ")
        prescription = input("Prescription: ")
        notes = input("Additional Notes: ")
