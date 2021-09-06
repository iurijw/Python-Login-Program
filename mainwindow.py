from tkinter import *
from typing import List
from models.user import User
import pickle


def login() -> None:
    if len(users) > 0:
        if user_entry.get() != '' and user_pass_entry.get() != '':
            if (user_entry.get(), user_pass_entry.get()) in [(x.user_name, x.user_pass) for x in users]:
                information.config(text='You have been logged in.', fg='green')
                for x in users:
                    if x.user_name == user_entry.get():
                        success_login_window(x)
            else:
                information.config(text='User or Pass is wrong.', fg='red')
        else:
            information.config(text='User and pass must be filled in.', fg='red')
    else:
        information.config(text='No users in database.', fg='red')


def success_login_window(x: User) -> None:
    # Success Login Window Settings
    success_login_window_tk: Tk = Tk()
    success_login_window_tk.geometry('250x250+1250+250')
    success_login_window_tk.title('User Data')

    #       Labels
    ######################

    # Initial Text
    userdata_text: Label = Label(success_login_window_tk, text='USER DATA', font=('Arial', 12), fg='black')
    userdata_text.place(relx=0.5, rely=0.1, anchor=CENTER)

    # Output Data
    success_username: Label = Label(success_login_window_tk, text=f'User ID: {x.id}\nUsername: {x.user_name}\n'
                                                                  f'Password: {x.user_pass}\nComment: {x.comment}',
                                    font=('Arial', 10))
    success_username.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Information Label
    info_data_label: Label = Label(success_login_window_tk, text='This is just a test output format for user data...',
                                   fg='red')
    info_data_label.place(relx=0.5, rely=0.9, anchor=CENTER)

    # Quit Button
    quit_button: Button = Button(success_login_window_tk, text='Quit',
                                 command=exit)
    quit_button.place(relx=0.5, rely=0.75, anchor=CENTER)


def register():

    def register_button_action():
        if register_user_entry.get() != '' and register_pass_entry.get() != '':
            if register_user_entry.get() != register_pass_entry.get():
                if register_user_entry.get() in [x.user_name for x in users]:
                    register_information_label.config(text="User already exists.", fg='red')
                else:
                    if users:
                        User.idf: int = max([x.id for x in users]) + 1
                    users.append(User(register_user_entry.get(), register_pass_entry.get(),
                                      register_comment_entry.get()))
                    with open('User_Database.pkl', 'wb') as f:
                        pickle.dump(users, f)
                    register_information_label.config(text="User registered with success.", fg='green')
            else:
                register_information_label.config(text="User and pass can't be the same.", fg='red')
        else:
            register_information_label.config(text='All information must be filled in.', fg='red')

    # Register Window Settings
    register_window = Tk()
    register_window.geometry('250x250+1250+250')
    register_window.title('Register')

    # Register Information Label
    register_information_label: Label = Label(register_window, text='', font=('Arial', 8))
    register_information_label.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Register Initial Text
    register_initial_text: Label = Label(register_window, text='Register Account', font=('Arial', 12))
    register_initial_text.place(relx=0.5, rely=0.1, anchor=CENTER)

    # Register User Label and Entry
    register_user_label: Label = Label(register_window, text='User: ', font=('Arial', 10))
    register_user_label.place(relx=0.2, rely=0.3, anchor=CENTER)
    register_user_entry: Entry = Entry(register_window, font=('Arial', 10))
    register_user_entry.place(relx=0.6, rely=0.30, anchor=CENTER)

    # Register Pass Label and Entry
    register_pass_label: Label = Label(register_window, text='Pass: ', font=('Arial', 10))
    register_pass_label.place(relx=0.2, rely=0.42, anchor=CENTER)
    register_pass_entry: Entry = Entry(register_window, font=('Arial', 10), show="*")
    register_pass_entry.place(relx=0.6, rely=0.42, anchor=CENTER)

    # Register Comment Label and Entry
    register_comment_label: Label = Label(register_window, text='Comment: ', font=('Arial', 10))
    register_comment_label.place(relx=0.18, rely=0.54, anchor=CENTER)
    register_comment_entry: Entry = Entry(register_window, font=('Arial', 10))
    register_comment_entry.place(relx=0.6, rely=0.54, anchor=CENTER)

    # Register Button
    register_button_to_register: Button = Button(register_window, text="Register", font=('Arial', 10),
                                                 command=register_button_action)
    register_button_to_register.place(relx=0.5, rely=0.85, anchor=CENTER)


if __name__ == '__main__':
    # Verify Users DB
    try:
        with open('User_Database.pkl', 'rb') as f:
            users: List[User] = pickle.load(f)
    except FileNotFoundError:
        users: List[User] = []

    # Main Window Settings
    main_window = Tk()
    main_window.geometry('200x200+1000+250')
    main_window.title('Login')

    #       Buttons, labels and entries settings
    #######################################################

    # Initial Text
    initial_text: Label = Label(main_window, text='LOGIN TEST PROGRAM', font=('Arial', 9))
    initial_text.place(relx=0.5, rely=0.126, anchor=CENTER)

    # User Label
    user: Label = Label(main_window, text='User', font=('Arial', 9))
    user.place(relx=0.02, rely=0.297, anchor=W)

    # User Entry
    user_entry: Entry = Entry(main_window, font=('Arial', 9))
    user_entry.place(relx=0.2, rely=0.3, anchor=W)

    # Pass Label
    user_pass: Label = Label(main_window, text='Pass', font=('Arial', 9))
    user_pass.place(relx=0.02, rely=0.43, anchor=W)

    # Pass Entry
    user_pass_entry: Entry = Entry(main_window, font=('Arial', 9), show="*")
    user_pass_entry.place(relx=0.2, rely=0.43, anchor=W)

    # Information Label
    information = Label(main_window, text='', font=('Arial', 8))
    information.place(relx=0.5, rely=0.60, anchor=CENTER)

    # Login Button
    login_button: Button = Button(main_window, text='Login', command=login)
    login_button.place(relx=0.225, rely=0.8, anchor=W)

    # Register Button
    register_button: Button = Button(main_window, text='Register', command=register)
    register_button.place(relx=0.525, rely=0.8, anchor=W)

    # Main Loop for Main Window
    main_window.mainloop()
