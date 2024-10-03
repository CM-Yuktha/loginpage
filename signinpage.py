from tkinter import *
from PIL import ImageTk, Image

# Function to hide the password
def hide():
    openeye.config(file='closedeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

# Function to show the password
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

# Placeholder behavior for username entry
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)
    usernameEntry.config(fg='black')

def user_leave(event):
    if usernameEntry.get() == '':
        usernameEntry.insert(0, 'Username')
        usernameEntry.config(fg='grey')

# Placeholder behavior for password entry
def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)
        passwordEntry.config(show='*', fg='black')

def password_leave(event):
    if passwordEntry.get() == '':
        passwordEntry.insert(0, 'Password')
        passwordEntry.config(show='', fg='grey')

# Simple validation for username and password
def validate_login():
    username = usernameEntry.get()
    password = passwordEntry.get()

    if username == 'Username' or username == '' or password == 'Password' or password == '':
        error_label.config(text="Please enter a valid username and password", fg='red')
    else:
        error_label.config(text="Login successful!", fg='green')
        # You can add actual login validation logic here.

# Initialize the main window
login_window = Tk()
login_window.geometry('998x660+50+50')
login_window.title('Login page using tkinter')

# Get screen dimensions
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()

login_window.geometry(f'{screen_width}x{screen_height}+0+0')

# Load and resize background image to fit the screen
bgImage = Image.open('image.jpg')
bgImage = bgImage.resize((screen_width, screen_height))
bgImage = ImageTk.PhotoImage(bgImage)

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch the image to cover the full window

# Center coordinates for the login form
form_x = int(screen_width/2 - 150)
form_y = int(screen_height/2 - 200)

# Create a semi-transparent frame (card) to hold the login form
card_frame = Frame(login_window, bg='#ffffff', bd=5)  # bd is the border width
card_frame.place(x=form_x - 25, y=form_y - 30, width=350, height=450)

card_frame.configure(bg='#ffffff', highlightthickness=0, relief='solid')
card_frame.tk_setPalette(background='#F5F5F5')  # Soft background color for the card

# Make the card semi-transparent using an rgba-like color (Tkinter doesn't support real alpha transparency)
card_frame.config(bg='#F5F5F5')

# Heading
heading = Label(card_frame, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='#F5F5F5', fg='black')
heading.pack(pady=10)

# Username Entry
usernameEntry = Entry(card_frame, width=20, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='grey')
usernameEntry.pack(pady=10)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)
usernameEntry.bind('<FocusOut>', user_leave)

Frame(card_frame, width=250, height=2, bg='black').pack(pady=5)

# Password Entry
passwordEntry = Entry(card_frame, width=20, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='grey')
passwordEntry.pack(pady=10)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
passwordEntry.bind('<FocusOut>', password_leave)

Frame(card_frame, width=250, height=2, bg='black').pack(pady=5)

# Eye button to show/hide password
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(card_frame, image=openeye, bd=0, bg='#F5F5F5', activebackground='#F5F5F5', cursor='hand2', command=hide)
eyeButton.place(x=250, y=140)  # Adjust this as needed

# Forgot password button
forgetButton = Button(card_frame, text='Forgot Password?', bd=0, bg='#F5F5F5', activebackground='#F5F5F5', cursor='hand2',
                      font=('Microsoft Yahei UI Light', 10, 'bold'), fg='black', activeforeground='black')
forgetButton.pack(pady=10)

# Error label for validation feedback
error_label = Label(card_frame, text='', font=('Microsoft Yahei UI Light', 10, 'bold'), fg='red', bg='#F5F5F5')
error_label.pack()

# Login Button
loginButton = Button(card_frame, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='black',
                     cursor='hand2', bd=0, width=19, command=validate_login)
loginButton.pack(pady=20)

# OR Label
orLabel = Label(card_frame, text='----------------OR----------------', font=('Open Sans', 16), fg='black', bd=0, bg='#F5F5F5')
orLabel.pack(pady=10)

# Signup option
signupLabel = Label(card_frame, text="Don't have an account?", font=('Open Sans', 10, 'bold'), fg='black', bd=0, bg='#F5F5F5')
signupLabel.pack()

newaccButton = Button(card_frame, text='Create new one', font=('Open Sans', 10, 'bold underline'), fg='black',
                      bg='#F5F5F5', cursor='hand2', bd=0)
newaccButton.pack()

# Start the GUI
login_window.mainloop()
