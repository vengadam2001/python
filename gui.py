'''
from tkinter import messagebox as a
ok=a.askyesno("prashanth","do you know python")
print("your reply is:",end="")
if ok:
    print("yes")
else:
    print("no")
    a.showwarning("god","you are going to fail be careful")
'''
''''''
from tkinter import Label,Tk,Button,messagebox
root=Tk()
root.title("my string")
msg=Label(root,text="welcome to sret")
msg.config(font=("arial black",30,"bold"))
msg.pack()
msgb=Button(root,text="exit",command=root.destroy)
msgb.pack()
def call():
    print("hello")
msgb1=Button(root,text="print hello",command=call)
msgb1.pack()
var=0
def call1():
    messagebox.askyesno("ques","do you know python")
    if var:
        messagebox.Dialog("good")
    else:
        messagebox.showwarning("be carefull you may fail")


msgb2=Button(root,text="ask",comamnd=call1())
msgb2.pack()
root.mainloop()
