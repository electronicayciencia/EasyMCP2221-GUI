import sys
import tkinter as tk
from tkinter import ttk
from time import sleep
from threading import Thread
from tkinter.messagebox import showinfo


class I2Cscan_window(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)        
        self.title("I2C Scan")
        self.devices_msg = []
        
        self.addr = tk.IntVar()
        self.scan_done = tk.IntVar(self, 0)

        self.transient(root)
        self.grab_set()

        #frame = tk.Frame(self).pack(padx=20, pady=20)

        #tk.Label(self, text="Searching address...").pack(padx=5, pady=5, anchor=tk.W)

        self.pb = ttk.Progressbar(self, orient="horizontal", length=250, mode="determinate")
        self.pb.pack(padx=5, pady=5)

        self.launch_scan()

        self.addr.trace("w", self.update_pb)
        self.scan_done.trace("w", self.show_devices)


    def update_pb(self, *args):
        self.pb["value"] = self.addr.get()


    def launch_scan(self):
        t = Thread(target=self.scan)
        t.start()


    def show_devices(self, *args):
        if len(self.devices_msg) == 0:
            showinfo("I2C Scan result","No devices found.")
        else:
            showinfo("I2C Scan result","\n".join(self.devices_msg))
            
        self.destroy()
    
    
    def scan(self):
        for i in range(0,100):
            self.addr.set(i)
            sleep(0.01)
            if i in (10, 50, 90):
                self.devices_msg.append("I2C slave found at address 0x%02X" % (i))
        self.scan_done.set(1)


class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()
        self.master = master

        self.button_bonus = ttk.Button(self, text="Bonuses", command=self.popup_bonus)
        self.button_bonus.pack(padx=20, pady=20)

    def popup_bonus(self):
        popup = I2Cscan_window(self)
        self.wait_window(popup)
        #self.master.destroy()
    

root = tk.Tk()

app = Application(root)

root.mainloop()