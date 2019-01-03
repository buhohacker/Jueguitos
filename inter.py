import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from PIL import Image, ImageTk

#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PlayPage, RulePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        path = "zz.png"
        #C:/Users/aecan/Documents/UPM/4º/OPTIMIZACION_Y_JUEGOS/PROYECTO/
        im = Image.open(path)
        ph = ImageTk.PhotoImage(im)

        label = tk.Label(self, image=ph, font=controller.title_font)
        label.image = ph  # need

        label.pack(side="top", fill="x", pady=10)

        playButton = tk.Button(self, bg="PaleGreen1", text="JUGAR",command=lambda: controller.show_frame("PlayPage"))
        # justify="center"
        ruleButton = tk.Button(self, bg="light blue", text="REGLAS",command=lambda: controller.show_frame("RulePage"))
        # , justify="center"
        # ,command=openRules()
        playButton.pack(side="left", expand="True")
        ruleButton.pack(side="right", expand="True")

        ##
        # button1 = tk.Button(self, text="Go to Page One",
        #                     command=lambda: controller.show_frame("PageOne"))
        #         # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
        # button1.pack()
        # button2.pack()

class PlayPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
        im = Image.open("background 1.png")
        background_image = ImageTk.PhotoImage(im)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.pack()
        self.crearNodos()
        print(self.adyacencias)
        
        
        

    def crearNodos(self):
        self.adyacencias = []
        self.nodos = []
        nodes = [line.rstrip('\n') for line in open('nivel1.txt')]
        for l in nodes:
            pos, ad = l.split(";")
            pos = pos.split(",")
            self.adyacencias.append([int(i) for i in ad.split(",")]) 
            im = Image.open("nodo.png")
            bu = ImageTk.PhotoImage(im)
            self.nodos.append(tk.Button(self, command = lambda: print(""), image = bu))
            self.nodos[-1].image = bu
            self.nodos[-1].place(x = int(pos[0]), y = 80 + int(pos[1]))
        
        
        
class RulePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()