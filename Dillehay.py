import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import ImageTk, Image

class LotChangeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lot Change Request")
        self.root.iconbitmap(r"C:\Users\jp462\OneDrive\Desktop\IVYTECH\PYTHON\M06\sticky_notes_icon_259264.ico")
        self.root.geometry("500x500")

        # Load the image
        image_path = "C:/Users/jp462/OneDrive/Desktop/IVYTECH/PYTHON/M08/paper_2.jpg"
        self.image = Image.open(image_path)
        self.image = self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)

        # Create the "Change Lot" button with image
        self.button_change_lot = tk.Button(root, text="Change Lot", compound="left", image=self.photo, command=self.change_lot)
        self.button_change_lot.pack(pady=50)

    def change_lot(self):
        response = messagebox.askyesno("Confirmation", "Are you sure the item number on the new DHR match the item number on the old DHR?")

        if response:
            messagebox.showinfo("Lot Change", "Proceeding to Forms.")
            self.open_forms_page()
        else:
            messagebox.showinfo("Lot Change", "Different item numbers usually mean different material or packaging.  Please check both DHRs before proceeding.")

    def open_forms_page(self):
        # Open Hyperlinks for Operator
        webbrowser.open("file:///path/to/forms_page.html")

class LotCloseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lot Close Request")
        self.root.iconbitmap(r"C:\Users\jp462\OneDrive\Desktop\IVYTECH\PYTHON\M06\sticky_notes_icon_259264.ico")
        self.root.geometry("500x500")

        # Load the image
        image_path = "C:/Users/jp462/OneDrive/Desktop/IVYTECH/PYTHON/M08/43624.jpg"
        self.image = Image.open(image_path)
        self.image = self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)

        # Create the "Close Lot" button with image
        self.button_close_lot = tk.Button(root, text="   Close Lot  ", compound="left", image=self.photo, command=self.close_lot)
        self.button_close_lot.pack(pady=50)

    def close_lot(self):
        response = messagebox.askyesno("Confirmation", "Is there any heldware in your current order that needs to be remade?")

        if response:
            messagebox.showinfo("Lot Close", "If there is any Heldware documented in your 'Label Control Record' page, please see a Quality Tech before closing the current order.")
            
        else:
            messagebox.showinfo("Lot Close", "Opening Forms.")
            self.open_forms_page()

    def open_forms_page(self):
        # Open Hyperlinks for Operator
        webbrowser.open("file:///path/to/forms_page.html")

class FeedbackApp:
    def __init__(self, root):
        self.root = tk.Toplevel(root)  # Create a Toplevel window for feedback
        self.root.title("Feedback")
        self.root.geometry("500x500")

        # Load the image
        image_path = "C:/Users/jp462/OneDrive/Desktop/IVYTECH/PYTHON/M08/icons8-feedback-50.png"
        self.image = Image.open(image_path)
        self.image = self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)

        # Create the "Feedback" button with image
        self.button_feedback = tk.Button(self.root, text="   Feedback  ", compound="left", image=self.photo, command=self.show_feedback_page)
        self.button_feedback.pack(pady=10)

        # Create a frame for feedback app
        self.frame = tk.Frame(self.root)

        # Create a label for feedback page
        self.label_feedback = tk.Label(self.frame, text="Welcome to the Feedback Page!")
        self.label_feedback.pack(pady=10)

        # Create an entry widget for feedback input
        self.entry_feedback = tk.Entry(self.frame, width=30)
        self.entry_feedback.pack(pady=10)

        # Create a label to display feedback
        self.display_feedback_label = tk.Label(self.frame, text="")
        self.display_feedback_label.pack(pady=10)

        # Store feedback entries in a dictionary
        self.feedback_entries = {}

    def show_feedback_page(self):
        # Create a new Toplevel window
        feedback_page = tk.Toplevel(self.root)
        feedback_page.title("Feedback")
        feedback_page.geometry("500x500")

        # Load the image for the feedback page
        image_path = "C:/Users/jp462/OneDrive/Desktop/IVYTECH/PYTHON/M08/icons8-feedback-50.png"
        image = Image.open(image_path)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)

        # Create a label for feedback page
        label_feedback = tk.Label(feedback_page, text="Welcome to the Feedback Page!")
        label_feedback.pack(pady=10)

        # Create an entry widget for feedback input
        entry_feedback = tk.Entry(feedback_page, width=30)
        entry_feedback.pack(pady=10)

        # Create a label to display feedback
        display_feedback_label = tk.Label(feedback_page, text="")
        display_feedback_label.pack(pady=10)

        # Store feedback entries in a dictionary
        feedback_entries = {}

        def feedback():
            user_feedback = entry_feedback.get()

            # Check if the feedback is not empty before storing
            if user_feedback:
                # Store the feedback in the dictionary
                feedback_id = len(feedback_entries) + 1
                feedback_entries[feedback_id] = user_feedback

                # Display the feedback on the label
                display_feedback_label.config(text=f"User Feedback: {user_feedback}")

                # Clear the entry widget after storing feedback
                entry_feedback.delete(0, tk.END)
            else:
                print("Please enter feedback.")

        # Create a button to submit feedback
        button_submit_feedback = tk.Button(feedback_page, text="Submit Feedback", command=feedback)
        button_submit_feedback.pack(pady=10)
        
def main():
    root = tk.Tk()

    # Create instances of both apps
    app_change = LotChangeApp(root)
    app_close = LotCloseApp(root)
    app_feedback = FeedbackApp(root)

    # Create a button to open the feedback page
    button_feedback = tk.Button(root, text="Give Feedback", command=app_feedback.root.deiconify)
    button_feedback.pack(pady=10)

    # Withdraw the feedback window
    app_feedback.root.withdraw()

    root.mainloop()

if __name__ == "__main__":
    main()
