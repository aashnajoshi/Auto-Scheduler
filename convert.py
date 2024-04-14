import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def convert_xlsx_to_csv():
    root = tk.Tk()
    root.withdraw() 

    while True:
        xlsx_file_path = filedialog.askopenfilename(parent=root, filetypes=[("Excel files", "*.xlsx")])
        if not xlsx_file_path:
            print("No file selected.")
            choice = messagebox.askyesno("Convert more files?", "Do you want to convert more files?")
            if not choice:
                break
            else:
                continue
        
        try:
            filename, _ = os.path.splitext(xlsx_file_path)
            data = pd.read_excel(xlsx_file_path)
            csv_file_path = filename + ".csv"
            data.to_csv(csv_file_path, index=False)
            print(f"Conversion successful: {xlsx_file_path} -> {csv_file_path}")
        except Exception as e:
            print(f"Error occurred: {e}")
        
if __name__ == "__main__":
    convert_xlsx_to_csv()