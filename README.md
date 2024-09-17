   Format : UID|DATA|DATA
---

# Facebook Live Uid Checker

## Description

**Facebook Live Uid Checker** is a Python GUI application built with `CustomTkinter` for processing bulk data to classify entries as "Active" or "Locked". The application reads data from a text file, makes HTTP requests to verify the status of each entry, and saves the results to separate files.

## Features

- Load input data from a file.
- Process each line of data to determine its status.
- Categorize data as "Active" or "Locked".
- Save the results to `ACTIVE.txt` and `DEATH.txt`.
- Display processing status and counts in the GUI.

## Requirements

- Python 3.x
- `requests`
- `customtkinter`
- `tkinter`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nill404-Cyber/LIVE-CHECKER-GUI.git
   cd LIVE-CHECKER-GUI
   ```

2. **Install required packages**:
   ```bash
   pip install requests tkinter customtkinter
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Load Input File**:
   - Click the "Load File" button and select the input text file.

3. **Start Processing**:
   - Click the "Start Checking" button to begin processing the data.

4. **View Results**:
   - The application will display the status of each entry and update the counts for "Active" and "Locked" entries.

## Example

To use the application, run it and follow the prompts to load an input file and start processing. The results will be displayed in the status text box, and the counts for "Active" and "Locked" entries will be updated.

---
