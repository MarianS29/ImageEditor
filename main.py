#env set up:
#pip install pillow ttkbootstrap

#import req libraries

import ttkbootstrap as ttk
from tkinter import filedialog
from tkinter.messagebox import showerror, askyesno
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab


#Global vars

WIDTH = 1600
HEIGHT = 700
file_path = ""
pen_size = 3
pen_color = "black"

#Functions

# function to open the image file
def open_image():
    global file_path
    file_path = filedialog.askopenfilename(title="Open Image File",
                                           filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    if file_path:
        global image, photo_image
        image = Image.open(file_path)
        WIDTH, HEIGHT = image.size
        raport = WIDTH/HEIGHT
        HEIGHT = 666
        WIDTH = (int)(raport*HEIGHT)
        image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor="nw", image=image)

# a global variable for checking the flip state of the image
is_flipped = False

def flip_image():
    try:
        global rotated_image, image, photo_image, is_flipped
        if not is_flipped:
            # open the image and flip it left and right
            image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT)
            is_flipped = True
        else:
            # reset the image to its original state
            image = Image.open(file_path)
            is_flipped = False
        # resize the image to fit the canvas
        WIDTH, HEIGHT = image.size
        raport = WIDTH / HEIGHT
        HEIGHT = 666
        WIDTH = (int)(raport * HEIGHT)
        image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        photo_image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor="nw", image=photo_image)

    except:
        showerror(title='Flip Image Error', message='Please select an image to flip!')


# global variable for tracking rotation angle
rotation_angle = 0


# function for rotating the image
def rotate_image():
    try:
        global image, photo_image, rotation_angle
        # open the image and rotate it

        image = Image.open(file_path)
        WIDTH, HEIGHT = image.size
        raport = WIDTH / HEIGHT
        HEIGHT = 666
        WIDTH = (int)(raport * HEIGHT)
        image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
        rotated_image = image.rotate(rotation_angle + 90)
        rotation_angle += 90
        # reset image if angle is a multiple of 360 degrees
        if rotation_angle % 360 == 0:
            rotation_angle = 0
            image = Image.open(file_path)
            WIDTH, HEIGHT = image.size
            raport = WIDTH / HEIGHT
            HEIGHT = 666
            WIDTH = (int)(raport * HEIGHT)
            image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
            rotated_image = image
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        photo_image = ImageTk.PhotoImage(rotated_image)
        canvas.create_image(0, 0, anchor="nw", image=photo_image)
    # catches errors
    except:
        showerror(title='Rotate Image Error', message='Please select an image to rotate!')

# function for applying filters to the opened image file
def apply_filter(filter):
    global image, photo_image
    try:
        # check if the image has been flipped or rotated
        if is_flipped:
            # flip the original image left and right
            flipped_image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT)
            # rotate the flipped image
            rotated_image = flipped_image.rotate(rotation_angle)
            # apply the filter to the rotated image
            if filter == "Black and White":
                rotated_image = ImageOps.grayscale(rotated_image)
            elif filter == "No Filter":
                rotated_image = image
            elif filter == "Update Image":
                rotated_image = image
            elif filter == "Blur":
                rotated_image = rotated_image.filter(ImageFilter.BLUR)
            elif filter == "Contour":
                rotated_image = rotated_image.filter(ImageFilter.CONTOUR)
            elif filter == "Detail":
                rotated_image = rotated_image.filter(ImageFilter.DETAIL)
            elif filter == "Emboss":
                rotated_image = rotated_image.filter(ImageFilter.EMBOSS)
            elif filter == "Edge Enhance":
                rotated_image = rotated_image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Sharpen":
                rotated_image = rotated_image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                rotated_image = rotated_image.filter(ImageFilter.SMOOTH)
            else:
                rotated_image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT).rotate(rotation_angle)
        elif rotation_angle != 0:
            # rotate the original image
            rotated_image = Image.open(file_path).rotate(rotation_angle)
            # apply the filter to the rotated image
            if filter == "Black and White":
                rotated_image = ImageOps.grayscale(rotated_image)
            elif filter == "No Filter":
                rotated_image = rotated_image
            elif filter == "Update Image":
                rotated_image = rotated_image
            elif filter == "Blur":
                rotated_image = rotated_image.filter(ImageFilter.BLUR)
            elif filter == "Contour":
                rotated_image = rotated_image.filter(ImageFilter.CONTOUR)
            elif filter == "Detail":
                rotated_image = rotated_image.filter(ImageFilter.DETAIL)
            elif filter == "Emboss":
                rotated_image = rotated_image.filter(ImageFilter.EMBOSS)
            elif filter == "Edge Enhance":
                rotated_image = rotated_image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Sharpen":
                rotated_image = rotated_image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                rotated_image = rotated_image.filter(ImageFilter.SMOOTH)
        else:
            # apply the filter to the original image
            image = Image.open(file_path)
            if filter == "Black and White":
                image = ImageOps.grayscale(image)
            elif filter == "Update Image":
                image = image
            elif filter == "No Filter":
                image = image
            elif filter == "Blur":
                image = image.filter(ImageFilter.BLUR)
            elif filter == "Sharpen":
                image = image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                image = image.filter(ImageFilter.SMOOTH)
            elif filter == "Emboss":
                image = image.filter(ImageFilter.EMBOSS)
            elif filter == "Detail":
                image = image.filter(ImageFilter.DETAIL)
            elif filter == "Edge Enhance":
                image = image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Contour":
                image = image.filter(ImageFilter.CONTOUR)
            rotated_image = image
        # resize the rotated/flipped image to fit the canvas
        WIDTH, HEIGHT = rotated_image.size
        raport = WIDTH / HEIGHT
        HEIGHT = 666
        WIDTH = (int)(raport * HEIGHT)
        rotated_image = rotated_image.resize((WIDTH, HEIGHT), Image.LANCZOS)
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        photo_image = ImageTk.PhotoImage(rotated_image)
        canvas.create_image(0, 0, anchor="nw", image=photo_image)
    except:
        showerror(title='Error', message='Please select an image first!')
#############################################


# function for drawing lines on the opened image
def draw(event):
    global file_path
    if file_path:
        x1, y1 = (event.x - pen_size), (event.y - pen_size)
        x2, y2 = (event.x + pen_size), (event.y + pen_size)
        canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline="", width=pen_size, tags="oval")

# function for changing the pen color
def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]


# function for erasing lines on the opened image
def erase_lines():
    global file_path
    if file_path:
        canvas.delete("oval")

# the function for saving an image
def save_image():
    global photo_image, file_path, is_flipped, rotation_angle
    if file_path:
        # create a new PIL Image object from the canvas
        image = Image.open(file_path)
        WIDTH, HEIGHT = image.size
        raport = WIDTH / HEIGHT
        HEIGHT = 666
        WIDTH = (int)(raport * HEIGHT)
        image = ImageGrab.grab(bbox=(canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + WIDTH, canvas.winfo_rooty() + HEIGHT))
        # check if the image has been flipped or rotated
        if is_flipped and rotation_angle % 360 != 0:
            WIDTH, HEIGHT = image.size
            raport = WIDTH / HEIGHT
            HEIGHT = 666
            WIDTH = (int)(raport * HEIGHT)
            image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image = image.rotate(rotation_angle)
            file_path = file_path.split(".")[0] + "_mod.jpg"
        if is_flipped or rotation_angle % 360 != 0:
            # Resize and rotate the image
            WIDTH, HEIGHT = image.size
            raport = WIDTH / HEIGHT
            HEIGHT = 666
            WIDTH = (int)(raport * HEIGHT)
            image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
            if is_flipped:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
                WIDTH, HEIGHT = image.size
                raport = WIDTH / HEIGHT
                HEIGHT = 666
                WIDTH = (int)(raport * HEIGHT)
                image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
            if rotation_angle % 360 != 0:
                # image = image.rotate(rotation_angle)
                WIDTH, HEIGHT = image.size
                raport = WIDTH / HEIGHT
                HEIGHT = 666
                WIDTH = (int)(raport * HEIGHT)
                image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
            # update the file path to include the modifications in the file name
            file_path = file_path.split(".")[0] + "_mod.jpg"
        # apply any filters to the image before saving
        filter = filter_combobox.get()
        if filter:
            if filter == "Black and White":
                image = ImageOps.grayscale(image)
            # elif filter == "Update Image":
            #     image = image
            elif filter == "No Filter":
                image = image
            elif filter == "Blur":
                image = image.filter(ImageFilter.BLUR)
            elif filter == "Sharpen":
                image = image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                image = image.filter(ImageFilter.SMOOTH)
            elif filter == "Emboss":
                image = image.filter(ImageFilter.EMBOSS)
            elif filter == "Detail":
                image = image.filter(ImageFilter.DETAIL)
            elif filter == "Edge Enhance":
                image = image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Contour":
                image = image.filter(ImageFilter.CONTOUR)
            # update the file path to include the filter in the file name
            file_path = file_path.split(".")[0] + "_" + filter.lower().replace(" ", "_") + ".jpg"
        # open file dialog to select save location and file type
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            if askyesno(title='Save Image', message='Do you want to save this image?'):
                # save the image to a file
                image.save(file_path)



#GUI

root = ttk.Window(themename="superhero")
root.title("Image Editor")
root.geometry("1300x700+300+110")
root.resizable(1, 1)
icon = ttk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)

# the left frame to contain the 4 buttons
left_frame = ttk.Frame(root, width=200, height=600)
left_frame.pack(side="left", fill="y")

# the right canvas for displaying the image
canvas = ttk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
# binding the Canvas to the B1-Motion event
canvas.bind("<B1-Motion>", draw)

############################### Aici referim filtrele care sunt partea principala din proiect

# label
filter_label = ttk.Label(left_frame, text="Select Filter:", background="#2b3e50")
filter_label.pack(padx=0, pady=1)

# a list of filters
image_filters = ["No Filter","Contour", "Black and White", "Blur", "Detail", "Emboss", "Edge Enhance", "Sharpen", "Smooth","Update Image"]

# combobox for the filters
filter_combobox = ttk.Combobox(left_frame, values=image_filters, width=15)
filter_combobox.current(0)
filter_combobox.pack(padx=10, pady=0)
filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))
#####################################################


# loading the icons for the 4 buttons
image_icon = ttk.PhotoImage(file = 'add.png').subsample(12, 12)
flip_icon = ttk.PhotoImage(file = 'flip.png').subsample(12, 12)
rotate_icon = ttk.PhotoImage(file = 'rotate.png').subsample(12, 12)
color_icon = ttk.PhotoImage(file = 'color.png').subsample(12, 12)
erase_icon = ttk.PhotoImage(file = 'erase.png').subsample(12, 12)
save_icon = ttk.PhotoImage(file = 'saved.png').subsample(12, 12)

# button for adding/opening the image file
image_button = ttk.Button(left_frame, image=image_icon, bootstyle="primary-outline", command=open_image)
image_button.pack(pady=22)
# button for flipping the image file
flip_button = ttk.Button(left_frame, image=flip_icon, bootstyle="info-outline", command=flip_image)
flip_button.pack(pady=22)
# button for rotating the image file
rotate_button = ttk.Button(left_frame, image=rotate_icon, bootstyle="warning-outline", command=rotate_image)
rotate_button.pack(pady=22)
# button for choosing pen color
color_button = ttk.Button(left_frame, image=color_icon, bootstyle="success-outline", command=change_color)
color_button.pack(pady=22)
# button for erasing the lines drawn over the image file
erase_button = ttk.Button(left_frame, image=erase_icon, bootstyle="light-outline", command=erase_lines )
erase_button.pack(pady=22)
# button for saving the image file
save_button = ttk.Button(left_frame, image=save_icon, bootstyle='danger-outline', command=save_image)
save_button.pack(pady=22)

root.mainloop()