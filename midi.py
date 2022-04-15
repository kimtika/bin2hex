import os
import tkinter
from tkinter import filedialog

def bin2hex():
    input_file_path=input_box.get()
    output_file_path=input_box2.get()+"/"+input_box3.get()+".txt"
    byteSize=os.path.getsize(input_file_path)
    with open(input_file_path, "rb") as f: 
        buf = f.read(byteSize).hex()
    with open(output_file_path, 'w') as f:
        for i in range(len(buf)//2):
            print(buf[2*i:2*i+2],end=" ",file=f)
    input_label5["text"]=(tkinter.END, "変換完了")


def file_select():
    idir = 'C:\\'
    filetype = [("すべて","*")]
    file_path = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = idir)
    input_box.insert(tkinter.END, file_path)
def file_select2():
    idir = 'C:\\'
    file_path = tkinter.filedialog.askdirectory(initialdir = idir)
    input_box2.insert(tkinter.END, file_path)

#ウインドウの作成
root = tkinter.Tk()
root.title("Python GUI")
root.geometry("560x320")

#入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=60)

#ラベルの作成
input_label = tkinter.Label(text="入力")
input_label.place(x=10, y=30)

#ボタンの作成
button = tkinter.Button(text="参照",command=file_select)
button.place(x=10, y=90)
#入力欄の作成
input_box2 = tkinter.Entry(width=40)
input_box2.place(x=10, y=150)
#ラベルの作成
input_label2 = tkinter.Label(text="出力先")
input_label2.place(x=10, y=120)

#ボタンの作成
button2 = tkinter.Button(text="参照",command=file_select2)
button2.place(x=10, y=180)
#入力欄の作成
input_box3 = tkinter.Entry(width=20)
input_box3.place(x=280, y=150)
input_box3.insert(0, "output")
#ラベルの作成
input_label3 = tkinter.Label(text="ファイル名")
input_label3.place(x=280, y=120)
#ラベルの作成
input_label4 = tkinter.Label(text=".txt")
input_label4.place(x=400, y=150)
#ボタンの作成
button3 = tkinter.Button(text="開始",command=bin2hex)
button3.place(x=350, y=180)
input_label5 = tkinter.Label(text="")
input_label5.place(x=10, y=250)
#ウインドウの描画
root.mainloop()