import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk


# Function to generate QR code and display it
def generate_qr_code():
    url = entry_url.get()  # Get the URL from the user input
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Save the QR code as an image file
    img.save("qrcode.png")

    # Open the image and display it in the GUI
    qr_img = Image.open("qrcode.png")
    qr_img = qr_img.resize((200, 200))  # Resize to fit the window
    qr_img = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img  # Keep a reference to avoid garbage collection

    messagebox.showinfo("Success", "QR Code generated and saved as 'qrcode.png'")


# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")  # Set the window size

# Create a label for the website URL
label_url = tk.Label(root, text="Enter Website URL:", font=("Arial", 14))
label_url.pack(pady=10)

# Create an entry widget to accept the URL
entry_url = tk.Entry(root, width=50, font=("Arial", 12))
entry_url.pack(pady=10)

# Create a button to generate the QR code
btn_generate = tk.Button(
    root, text="Generate QR Code", command=generate_qr_code, font=("Arial", 14)
)
btn_generate.pack(pady=20)

# Label to display the generated QR code image
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Run the application
root.mainloop()
