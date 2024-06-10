import cv2
import tkinter as tk
from tkinter import filedialog

def resize_image():
    source = filedialog.askopenfilename(title="Select Image")
    if not source:
        return

    destination = filedialog.asksaveasfilename(title="Save As", defaultextension=".png")
    if not destination:
        return

    scale_percent = scale.get()

    src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

    # calculate the percentage of the original dimensions
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    # resize image
    output = cv2.resize(src, (new_width, new_height))

    cv2.imwrite(destination, output)

    result_label.config(text="Image resized and saved successfully!")

# Create main window
root = tk.Tk()
root.title("Image Resizer")

# Create widgets
label = tk.Label(root, text="Scale Percentage:")
label.pack(pady=10)

scale = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, length=200)
scale.set(50)
scale.pack(pady=10)

resize_button = tk.Button(root, text="Resize Image", command=resize_image)
resize_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()