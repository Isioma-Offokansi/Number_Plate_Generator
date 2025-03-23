# Number_Plate_Generator

A number plate generator that conforms to a set off specific rules.

## Features

- Generates number plates in the format: `Memory Tag Age Identifier Random Letters`
  - **Memory Tag**: Two letters chosen by the user.
  - **Age Identifier**: Two digits derived from the registration date.
  - **Random Letters**: Three randomly generated letters, excluding `I` and `Q`.
- Ensures uniqueness of number plates by storing previously generated plates in `License_Plates.txt`.
- Validates user input for memory tags and registration dates.
- Prevents registration of vehicles with years `XX50` or greater.

## Assumptions

- Cars with the year `XX50` or greater cannot be registered.
- The program uses a file named `License_Plates.txt` to store generated number plates.
- The program is designed to be run interactively, prompting the user for input.

## How It Works

1. The user is prompted to enter:
   - A memory tag (two letters).
   - A registration date in the format `DD/MM/YYYY`.
2. The program validates the input:
   - Ensures the memory tag is exactly two letters.
   - Ensures the date is valid and plausible.
3. The program calculates the age identifier based on the registration date:
   - If the month is between March and August, the age identifier is the last two digits of the year.
   - If the month is between September and February, the age identifier is the last two digits of the year plus 50.
4. The program generates three random letters, ensuring they do not include `I` or `Q`.
5. The program checks if the generated number plate is unique:
   - If not, it regenerates the random letters until a unique plate is created.
6. The unique number plate is stored in `License_Plates.txt`.

## File Structure

- `License_Plates.txt`: Stores all previously generated number plates.
- `Number_Plate_Generator.py`: The main script for generating number plates.

## Usage

1. Run the script `Number_Plate_Generator.py` in a Python environment.
2. Follow the prompts to enter the memory tag and registration date.
3. The program will generate and display the number plate if the input is valid.
4. The generated number plate will be saved in `License_Plates.txt`.

## Example

### Input:
>>> Enter information for a new number plate? [y/n]: y

>>> Enter a memory tag: AB Enter the date the car was registered (Format DD/MM/YYYY): 15/09/2023

### Output:
Number plate registered successfully!

### Generated Plate:
AB73 XYZ

## Requirements

- Python 3.x
- No additional libraries are required.

## Notes

- The program ensures that no duplicate number plates are generated.
- The `License_Plates.txt` file must exist in the same directory as the script.
