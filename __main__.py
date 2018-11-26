import tkinter as tk
import os
import sys
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from converter import *
import argparse

global file_in, file_out


def open_file():
    """
    ask user for filepath of the .csv
    :return: filepath
    """
    global file_in
    filename = askopenfile(filetypes=[("CSV files", "*.csv")])
    if filename:
        file_in = filename.name


def output_location():
    """
    ask user where to store the .vcf
    :return: filepath
    """
    global file_out
    filename = asksaveasfile(mode="w", defaultextension=".vcf")
    if filename:
        file_out = filename.name


def convert():
    global file_in, file_out
    c = Converter(file_in, file_out)
    c.convert()
    messagebox.showinfo("Conversion successful", "Successfully converted the CSV!")


if __name__ == "__main__":
    # switch modes
    # console
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Convert CSV to VCF")
        parser.add_argument('-in', dest='file', help='Input File Name', required=True)
        parser.add_argument('-out', dest='out', help='Output Path for VCF', default='contacts.vcf')
        args = parser.parse_args()

        file_in = args.file
        file_out = args.out

        c = Converter(file_in, file_out)
        c.convert()


    # gui
    else:
        root = tk.Tk()
        root.geometry("400x400")
        frame = tk.Frame(root).pack()

        label_1 = tk.Label(root, text="CSV2VCF-Converter", font=("arial", 30, "bold")).pack()

        button1 = tk.Button(frame, text="Input File", command=open_file).pack()
        button2 = tk.Button(frame, text="Output File", command=output_location).pack()
        button3 = tk.Button(frame, text="Convert!", command=convert).pack()

        root.mainloop()
