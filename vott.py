import tkinter as tk
from tkinter import messagebox

class VotingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Voting System")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.votes = {}  # Store votes with admission number as key

        # Create GUI Elements
        self.label = tk.Label(root, text="Enter your admission number:", font=('Helvetica', 14), bg="#f0f0f0")
        self.label.pack(pady=20)

        self.admission_entry = tk.Entry(root, font=('Helvetica', 14))
        self.admission_entry.pack(pady=10)

        self.photo_label = tk.Label(root, text="Click on the photo number to vote:", font=('Helvetica', 14), bg="#f0f0f0")
        self.photo_label.pack(pady=10)

        self.create_photo_buttons()

        self.results_button = tk.Button(root, text="View Results", command=self.display_results, font=('Helvetica', 14), bg="#4CAF50", fg="white")
        self.results_button.pack(pady=20)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=('Helvetica', 14), bg="#f44336", fg="white")
        self.exit_button.pack(pady=10)

    def create_photo_buttons(self):
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        # Create buttons for 15 photos (represented by their numbers) in a grid layout
        for i in range(1, 16):
            btn = tk.Button(button_frame, text=f"Photo {i}", command=lambda i=i: self.submit_vote(i), font=('Helvetica', 12), width=10)
            btn.grid(row=(i-1)//5, column=(i-1)%5, padx=10, pady=10)

    def submit_vote(self, photo_choice):
        admission_number = self.admission_entry.get()

        if admission_number in self.votes:
            messagebox.showwarning("Already Voted", "You have already voted!")
        elif not admission_number:
            messagebox.showwarning("No Admission Number", "Please enter your admission number.")
        else:
            self.votes[admission_number] = photo_choice
            messagebox.showinfo("Vote Submitted", f"Your vote for Photo {photo_choice} has been recorded. Thank you!")
            self.admission_entry.delete(0, tk.END)

    def display_results(self):
        results = {i: 0 for i in range(1, 16)}

        for photo_choice in self.votes.values():
            results[photo_choice] += 1

        results_text = "\n".join([f"Photo {photo}: {count} votes" for photo, count in results.items()])
        messagebox.showinfo("Voting Results", results_text)

# Create the main window
root = tk.Tk()
app = VotingSystem(root)
root.mainloop()
