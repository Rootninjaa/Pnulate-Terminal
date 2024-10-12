import os
import requests
import qrcode
from tkinter import Tk, filedialog
import webbrowser
import time
import random
import getpass
from datetime import datetime
from tqdm import tqdm

logo = ("""
  ____              _       _       
 |  _ \ _ __  _   _| | __ _| |_ ___ 
 | |_) | '_ \| | | | |/ _` | __/ _ \\
 |  __/| | | | |_| | | (_| | ||  __/
 |_|   |_| |_|\__,_|_|\__,_|\__\___|
        
GitHub: https://github.com/Rootninjaa/Pnulate-Terminal
Contact: rootlockinc@gmail.com
--help: all command
                                     
""")#I used the logo this way because the program was breaking otherwise and I used it this way to fix it.

def system_info():
    print("===== System Information =====")
    print(f"Operating System: {os.name}")
    user = getpass.getuser()
    print(f"User: {user}")
    current_directory = os.getcwd()
    print(f"Current Directory: {current_directory}")
    cpu_count = os.cpu_count()
    print(f"CPU Core Count: {cpu_count}")
    print("==============================")

def fetch_html_code(url):
    root = Tk()
    root.withdraw()

    try:
        response = requests.get(url)

        if response.status_code == 200:
            for _ in tqdm(range(6), unit="second", desc="Fetching HTML", colour="#660099"):
                time.sleep(1)
            print("Completed")

            file_path = filedialog.asksaveasfilename(
                defaultextension=".html",
                filetypes=[("HTML files", "*.html")],
                title="Save HTML Code"
            )

            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                print(f"HTML saved to {file_path}")
            else:
                print("Save operation canceled.")
        else:
            print(f"Failed to fetch URL: {response.status_code}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        root.destroy()

def view_file_content(file_name):
    if os.path.isfile(file_name):
        try:
            print("Reading file...")
            # Use a single progress bar for the file reading
            with tqdm(total=1, unit="file", desc="File reading", colour="#660099") as pbar:
                # Simulate a delay (if needed)
                time.sleep(1)  # Adjust the sleep time as necessary

                # Read the file content
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()

                pbar.update(1)  # Update the progress bar after reading the file
            
            print("Completed")  # Reading operation completed message
            print(f"Content:\n")
            print(content)

        except Exception as e:
            print(f"Failed to read file: {e}")
    else:
        print(f"Error: '{file_name}' not found.")

def create_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    dialog = Tk()
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Save QR Code"
        )
        
        if file_path:
            img.save(file_path)
            print(f"QR code saved as '{file_path}'.")
        else:
            print("ERROR 637: QR code not saved.")
    finally:
        dialog.destroy()

def open_browser(url):
    try:
        if url:
            webbrowser.open(url)
            print(f"Opening URL: {url}")
        else:
            print("ERROR 638: URL not provided.")
    except Exception as e:
        print(f"Failed to open URL: {e}")

def delete_file(file_name):
    if os.path.isfile(file_name): 
        try:
            os.remove(file_name)
            print(f"File '{file_name}' has been deleted.")
        except Exception as e:
            print(f"Failed to delete file: {e}")
    else:
        print(f"Error: '{file_name}' not found.")

def list_files(directory):
    for _ in tqdm(range(6), unit="second", desc="files are listed", colour="#660099"):
        time.sleep(3)
        print("Completed")

    if os.path.isdir(directory):
        try:
            files = os.listdir(directory)
            if files:
                print(f"Files in '{directory}':")
                for file in tqdm(files, desc="Listing files"):
                    print(file)
            else:
                print(f"No files found in '{directory}'.")
        except Exception as e:
            print(f"Failed to list files: {e}")
    else:
        print(f"Error: '{directory}' not found or not a directory.")

def generate_random_password():
    number_list = ["10", "20", "19", "30", "1"]
    suffix_list = ["byterminal", "bypluxee", "hoodbyegood"]
    number = random.choice(number_list)
    suffix = random.choice(suffix_list)
    print(f"Password: {number + suffix}")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Terminal cleared.")

def create_text_file():
    file_name = input("Enter new file name (e.g., file.txt): ")
    content = input("Enter file content: ")

    try:
        print("Creating file...")
        
        # Simulate the file creation process with a progress bar
        with tqdm(total=6, unit="second", desc="File creating", colour="#660099") as pbar:
            for _ in range(6):
                time.sleep(1)  # Simulating time taken to create the file
                pbar.update(1)  # Update the progress bar

        # Write content to the file after simulating the progress
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"File '{file_name}' created.")
        
    except Exception as e:
        print(f"Failed to create file: {e}")

print(logo)

def show_current_date_time():
    now = datetime.now()
    print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

while True:
    command = input("Pnulate:~$ ")
    
    if command == "--help":
        print("--kill terminal = quit the terminal")
        print("--help = all commands help")
        print("--show <file_name or file path> = show content of a file")
        print("--qr <url> = generate a QR code for the provided URL and open a file dialog to save it")
        print("--gethtml5lib <url> = returns the HTML codes of the site whose URL is written")
        print("--openwebsite <url> = opens the site you want")
        print("--deletefile <file_name or path> = deletes the specified file")
        print("--listfiles <directory_path> = lists all files in the specified directory")
        print("--genpass = generates a random password")
        print("--clear = clears the terminal")
        print("--neofetch = displays system properties")
        print("--createfile = creates a new text file")
        print("--datetime = displays the current date and time")
        

    elif command == "--kill terminal":
        print("Terminal killed.")
        break
    
    elif command.startswith("--show "):
        file_name = command[len("--show "):].strip()
        view_file_content(file_name)

    elif command.startswith("--qr "):
        url = command[len("--qr "):].strip()
        create_qr_code(url)
    
    elif command.startswith("--gethtml5lib "):
        url = command[len("--gethtml5lib "):].strip()
        fetch_html_code(url)

    elif command.startswith("--openwebsite "):
        url = command[len("--openwebsite "):].strip()
        open_browser(url)

    elif command.startswith("--deletefile "):
        file_name = command[len("--deletefile "):].strip()
        delete_file(file_name)

    elif command.startswith("--listfiles "):
        directory = command[len("--listfiles "):].strip()
        list_files(directory)

    elif command == "--genpass":
        generate_random_password()  

    elif command == "--clear":
        clear_terminal()

    elif command == "--neofetch":
        system_info()

    elif command == "--createfile":
        create_text_file()

    elif command == "--datetime":
        show_current_date_time()
    
    else:
        print("ERROR 323: is not recognized as an internal or external command")

input(".")
