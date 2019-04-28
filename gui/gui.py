from tkinter.filedialog import askopenfilename
import tkinter
import os
from PIL import ImageTk, Image
from v2def import generateDef as gdf

verilogfile = ""
leffile=""
libraryfile=""
deffile=""
speffile=""
dir_path=""
e1=0
e2=0
e3=0
e4=0
e5=0
e6=0
e7=0
e8=0
e9=0
e10=0

#This is where we lauch the verilogfile manager bar.
def OpenVerilogFile():
    global verilogfile
    verilogfile = askopenfilename(initialdir=dir_path,
                           filetypes =(("Verilog File", "*.v"),("All Files","*.*")),
                           title = "Choose a Verilog file."
                           )

#This is where we lauch the libraryfile manager bar.
def OpenLibFile():
    global libraryfile
    libraryfile = askopenfilename(initialdir=dir_path,
                           filetypes =(("Library File", "*.lib"),("All Files","*.*")),
                           title = "Choose a Verilog file."
                           )

#This is where we lauch the leffile manager bar.
def OpenLefFile():
    global leffile
    leffile = askopenfilename(initialdir=dir_path,
                           filetypes =(("Lef File", "*.lef"),("All Files","*.*")),
                           title = "Choose a Verilog file."
                           )

#generate def
def GnerateDef():
    deffile=verilogfile[:-2]+'.def'
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10
    try:
        print(gdf(verilogfile,libraryfile,leffile,deffile,optional= {'-a': e1.get(),'-u':
               e2.get(), '-s': e3.get(), '-h': e4.get(), '-mh': e5.get(),'-mv': e6.get(),'gnd_metal':
                e9.get(),'gnd_width': e10.get(),'vdd_metal': e7.get(),'vdd_width':e8.get()}))
    except:
       pass


dir_path = os.path.dirname(os.path.realpath(__file__))
root = tkinter.Tk()

canv = tkinter.Canvas(root, width=200, height=200, bg='black')
canv.grid(row=14, column=2)

img = ImageTk.PhotoImage(Image.open("vlsi.jpg"))  # PIL solution
canv.create_image(200, 200, image=img)


Title = root.title( "Samanoudy DEF Generator Tool")
verilogbut = tkinter.Button(canv,
                   text="Import Verilog File",
                   fg="blue",
                   width=15,
                   command=OpenVerilogFile)
verilogbut.grid(row=0, column=0)

lefbut = tkinter.Button(canv,
                   text="Import Lef File",
                    fg="blue",
                    width=15,
                   command=OpenLefFile)
lefbut.grid(row=2, column=0)

libbut = tkinter.Button(canv,
                   text="Import Library File",
                   fg="blue",
                   width=15,
                   command=OpenLibFile)
libbut.grid(row=1, column=0)


generatedefbut = tkinter.Button(canv,
                   text="Generate DEF File",
                   fg="green",
                   width=20,
                   height= 5,
                   command=GnerateDef)
generatedefbut.grid(row=0, column=1)

tkinter.Label(canv, text="Aspect Ratio").grid(row=4, column=0)
tkinter.Label(canv, text="Core Utilization").grid(row=5, column=0)
tkinter.Label(canv, text="Core Site width").grid(row=6, column=0)
tkinter.Label(canv, text="Core row height").grid(row=7, column=0)
tkinter.Label(canv, text="Horizontal Margin").grid(row=8, column=0)
tkinter.Label(canv, text="Vertical Margin").grid(row=9, column=0)
tkinter.Label(canv, text="VDD Metal Layer").grid(row=10, column=0)
tkinter.Label(canv, text="VDD Width").grid(row=11, column=0)
tkinter.Label(canv, text="GND Metal Layer").grid(row=12, column=0)
tkinter.Label(canv, text="GND Width").grid(row=13, column=0)

e1 = tkinter.Entry(canv)
e2 = tkinter.Entry(canv)
e3 = tkinter.Entry(canv)
e4 = tkinter.Entry(canv)
e5 = tkinter.Entry(canv)
e6 = tkinter.Entry(canv)
e7 = tkinter.Entry(canv)
e8 = tkinter.Entry(canv)
e9 = tkinter.Entry(canv)
e10 = tkinter.Entry(canv)

e1.grid(row=4, column=1)
e2.grid(row=5, column=1)
e3.grid(row=6, column=1)
e4.grid(row=7, column=1)
e5.grid(row=8, column=1)
e6.grid(row=9, column=1)
e7.grid(row=10, column=1)
e8.grid(row=11, column=1)
e9.grid(row=12, column=1)
e10.grid(row=13, column=1)


root.mainloop()
