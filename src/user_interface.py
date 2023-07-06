```python
import tkinter as tk
from tkinter import filedialog, messagebox
from src import data_import, email_generation, donor_segmentation, call_to_action, online_donation, recurring_donation

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fundraising Automation for Charity")
        self.upload_button = tk.Button(self.root, text="Upload Excel", command=self.upload_file)
        self.upload_button.pack()
        self.email_template_config = tk.Entry(self.root)
        self.email_template_config.pack()
        self.donation_progress = tk.Label(self.root, text="")
        self.donation_progress.pack()

    def upload_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if filename:
            try:
                donor_data = data_import.import_data(filename)
                high_level_donors, low_level_donors = donor_segmentation.segment_donors(donor_data)
                email_templates = self.email_template_config.get()
                for donor in high_level_donors:
                    email = email_generation.generate_email(donor, email_templates)
                    call_to_action.schedule_call(email)
                for donor in low_level_donors:
                    email = email_generation.generate_email(donor, email_templates)
                    online_donation.make_online_donation(email)
                    recurring_donation.promote_recurring_donation(email)
                self.donation_progress.config(text="Fundraising process completed successfully.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()

def init_ui():
    ui = UserInterface()
    ui.run()

if __name__ == "__main__":
    init_ui()
```