import customtkinter as ctk
from PIL import ImageTk
import tkinter as tk
import qrcode

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Initialize app window
        self.geometry('520x620')
        self.title('QR Generator')
        self.resizable(False, False)

        # Image view frame
        self.frame = ctk.CTkFrame(self, width=490, height=510, corner_radius=5)
        self.frame.place(relx=0.5, y=270, anchor=tk.CENTER)

        # Image label
        self.label = ctk.CTkLabel(self.frame, text='Enter some input to generate QR Code')
        self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Save status label
        self.label_saved = ctk.CTkLabel(self.frame, text=None)
        self.label_saved.place(relx=0.5, rely=0.95)

        # Input entry
        self.input = ctk.CTkEntry(self, placeholder_text='Enter address here...', width=490, corner_radius=5)
        self.input.bind('<Return>', self.generate_enter)
        self.input.place(relx=0.5, y=545, anchor=tk.CENTER)

        # Buttons
        self.generate_button = ctk.CTkButton(self, width=240, corner_radius=5, text='Generate Qr Code', command=self.generate)
        self.generate_button.place(relx=0.265, y=590, anchor=tk.CENTER)
        self.save_button = ctk.CTkButton(self, width=240, corner_radius=5, text='Save QR Code', command=self.save)
        self.save_button.place(relx=0.735, y=590, anchor=tk.CENTER)

    def generate_enter(self, event):
        self.generate()

    def generate(self):

        # Initialize QR code object
        self.qr = qrcode.QRCode(
            version=1,
            box_size=13, 
            border=1
        )

        # Add data and generate qrcode image
        self.qr.add_data(self.input.get())
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color='black', back_color='white')

        # Convert image to tkinter understand-able format
        img = ImageTk.PhotoImage(img)

        # Anchor and display image in label
        self.label.image = img
        self.label.configure(image=img)

        # Remove save status label
        self.label_saved.configure(text='')
    
    def save(self):

        # Generate QR Code to save
        qr = qrcode.make(self.input.get())
        # Prompt user for filename
        dialog = ctk.CTkInputDialog(master=None, text='Enter file name to save:', title='Save Qr Code')
        # Save QR Code to file
        qr.save(f"qr/{dialog.get_input()}.png")

        # Display save status
        self.label_saved = ctk.CTkLabel(self.frame, text='QR Code has ben saved!')
        self.label_saved.place(relx=0.5, rely=0.98, anchor=tk.CENTER)


app = App()
app.mainloop()