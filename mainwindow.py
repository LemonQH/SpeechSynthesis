import tkinter as tk
from tkinter import filedialog,messagebox,ttk
from synthesis import Synthesis_model
import os

syn_m=Synthesis_model("","","")

def get_files():
    files = filedialog.askopenfilenames(filetypes=[('text files', '.txt')])
    print(files)
    syn_m.file_paths=files
    if files:
        for file in files:
            text1.insert(tk.END, file + '\n')
            text1.update()
    else:
        print('你没有选择任何文件')

def synthesis_files():
    if syn_m.file_paths:
        message=syn_m.get_synthesis_result()
        tk.messagebox.showinfo("提示", message)
        os.system('start' + '.\\result')
        # if message=="1":
        #     print(1)
        #     os.system('start'+'.\\result')
        # else:
        #     tk.messagebox.showinfo("error",message)
    else :
        tk.messagebox.showinfo("提示","无文件")


root=tk.Tk()
root.title("youdao speech synthesis test")
frm = tk.Frame(root)
frm.grid(padx='50', pady='50')
btn_get_file = tk.Button(frm, text='选择待合成文件', command=get_files)
btn_get_file.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
text1 = tk.Text(frm, width='40', height='10')
text1.grid(row=0, column=1)

btn_sure=tk.Button(frm,text="合成",command=synthesis_files)
btn_sure.grid(row=1,column=1)


root.mainloop()
