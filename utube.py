from tkinter import *
from pytube import *
from tkinter.filedialog import *
from tkinter.messagebox import *

def index():
    Dialog.withdraw()
    resolution=var.get()
    path=askdirectory()
    if path==None:
        return
    resolution.download(path,filename="My_video")
    print("done")
    showinfo("Download Finished","Your video has been downloaded successfully")
    linkvalue.delete(0,END)

#https://www.youtube.com/watch?v=87uPLRXL3P8

def New():
    if linkvalue.get()=='':
        showerror("ValueError","Please enter a youtube video link")
        quit()
    Dialog=Toplevel(root)
    Dialog.title("Video Downloader")
    Dialog.geometry("700x600")
    Label(Dialog,text="Details of your  video",font=("lucida",12,"bold","italic")).pack(side="top")
    url = linkvalue.get()
    yt = YouTube(str(url))
    Label(Dialog,text=f"{yt.title}",padx=10)
    print("Title of video:   ", yt.title)
    print("Number of views:  ", yt.views)
    print("Length of video:  ", yt.length, "seconds")
    videos = yt.streams.filter(progressive=True).all()
    global var
    var = StringVar()
    var.set(videos[0])
    for video in videos:
        radio = Radiobutton(Dialog, text=f"{video}", font=("comicsansns",10,"bold","italic"),padx=20, variable=var, value=video).pack(anchor="w")
    Btn=button(Dialog,text="Select",padx=15,command=index).pack(side="right",anchor="ne")

root=Tk()
root.minsize(500,400)
root.geometry("900x600")
root.maxsize(1000,700)
logo=PhotoImage(file="logpreview.png")
logo_label=Label(root,image=logo,pady=8,padx=5).pack(side="top",anchor="nw")
root.title("VideoDownloader")
head=Label(root,text=" Youtube Video Downloader",font=("comicsansns",11,"bold","italic"),padx=5).pack(side="left",anchor="nw")
linkvalue=Label(root,text="Enter Youtube Video link ",font=("comicsansns",14,"italic"),padx=200).pack(side="top",anchor="nw")
linkvalue=StringVar()
linkentry=Entry(root,textvariable=linkvalue,font=("comicsansns",14,"italic")).pack(fill=X,padx=50,pady=20)
button=Button(root,text="Download",padx=30,pady=8,relief=RIDGE,command=New).pack(side="top",anchor="ne",padx=50)
root.mainloop()
