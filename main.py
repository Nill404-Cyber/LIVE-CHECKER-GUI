import requests
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog

class BulkDataProcessor:
    def __init__(self, input_file, errors_file="errors.txt"):
        self.input_file = input_file
        self.errors_file = errors_file
        self.active_count = 0
        self.locked_count = 0
    def status(self, data):
        try:
            idp, pasx, keyx = data.strip().split('|')
            response = str(requests.get(f'https://graph.facebook.com/{idp}/picture?type=normal').text)
            if 'Photoshop' in response:
                result = 'Active'
                self.active_count += 1
            else:
                result = 'Locked'
                self.locked_count += 1
            return data, result
        except Exception as e:
            return data, f'Error: {str(e)}'
    def process_bulk_data(self, status_text, update_counts):
        with open(self.input_file, 'r') as infile, \
             open(self.errors_file, 'a') as errors_outfile:
            lines = infile.readlines()
            for line in lines:
                data, result = self.status(line)
                if result == 'Active':
                    status_text.insert(tk.END, f"ACTIVE: {data}")
                    open('ACTIVE.txt','a').write(data)
                elif result == 'Locked':
                    status_text.insert(tk.END, f"DEAD: {data}")
                    open('DEATH.txt','a').write(data)
                else:
                    status_text.insert(tk.END, f"Error processing data: {data} - {result}\n")
                    errors_outfile.write(f"{data} - {result}\n")
                print(f"Processing data: {data} - {result}")
                update_counts(self.active_count, self.locked_count)
                status_text.yview(tk.END)  
                status_text.update_idletasks()  

class LiveCheckerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LIVE CHECKER")
        self.geometry("500x650")
        self.iconbitmap("favicon.ico")
        self.create_widgets()
    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="LIVE CHECKER", font=("Arial", 25))
        self.label.pack(pady=10)
        self.load_button = ctk.CTkButton(self, text="Load File", command=self.load_files)
        self.load_button.pack(pady=10)
        self.process_button = ctk.CTkButton(self, text="Start Checking", command=self.process_data)
        self.process_button.pack(pady=10)
        self.status_text = ctk.CTkTextbox(self, height=300, width=490)
        self.status_text.pack(pady=10)
        self.active_count_label = ctk.CTkLabel(self, text="Active : 0", font=("Arial", 20))
        self.active_count_label.pack(pady=5)
        self.locked_count_label = ctk.CTkLabel(self, text="Locked : 0", font=("Arial", 20))
        self.locked_count_label.pack(pady=5)
        self.input_file = None
    def load_files(self):
        self.input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])
        if self.input_file:
            self.status_text.insert(tk.END, f"Files loaded:\nInput: {self.input_file}\n")
        else:
            pass
    def process_data(self):
        if not self.input_file:
            pass
            return
        processor = BulkDataProcessor(self.input_file)
        self.status_text.insert(tk.END, "\nProcessing started...\n")
        self.update_idletasks()
        try:
            processor.process_bulk_data(self.status_text, self.update_counts)
            self.status_text.insert(tk.END, "\nProcessing completed.\n")
        except Exception as e:
            self.status_text.insert(tk.END, f"Error: {str(e)}\n")
    def update_counts(self, active_count, locked_count):
        self.active_count_label.configure(text=f"Active Count: {active_count}")
        self.locked_count_label.configure(text=f"Locked Count: {locked_count}")


if __name__ == "__main__":
    app = LiveCheckerApp()
    app.mainloop()
