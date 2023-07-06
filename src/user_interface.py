```python
import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
from src import data_import, email_generation, donor_segmentation, call_scheduling, online_donation, recurring_donation

def initUI():
    root = tk.Tk()
    root.title("Fundraising Automation for Charity")

    canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    upload = tk.Button(root, text="Upload Excel File", padx=10, pady=5, fg="white", bg="#263D42", command=addExcel)
    upload.pack()

    run = tk.Button(root, text="Run Automation", padx=10, pady=5, fg="white", bg="#263D42", command=runAutomation)
    run.pack()

    progress = tk.Label(root, text="Progress: 0%", bg="white")
    progress.pack()
    root.mainloop()

def addExcel():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
    donor_data = data_import.importData(filename)
    messagebox.showinfo("File Info", "Excel file uploaded successfully")

def runAutomation():
    email_generation.generateEmail(donor_data)
    high_level_donors, low_level_donors = donor_segmentation.segmentDonors(donor_data)
    call_scheduling.scheduleCall(high_level_donors)
    online_donation.makeOnlineDonation(low_level_donors)
    recurring_donation.promoteRecurringDonation(low_level_donors)
    progress['text'] = "Progress: 100%"
    messagebox.showinfo("Success", "Fundraising automation completed successfully")

if __name__ == "__main__":
    initUI()
```