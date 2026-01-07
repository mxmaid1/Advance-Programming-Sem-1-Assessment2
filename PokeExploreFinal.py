import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io


backgroundcolor="#2b0f3f"
backgroundcolorlighter="#3a145a"
panelcolorlight="#f0b429"
panelcolordark="#d99a1c"
panelcolordarker="#ff7b00"
innercolor="#ffffff"
lighttextcolor1="#ffffff"
darktextcolor1="#1b0e2a"
class CreateGuiApp:
    def __init__(self):
        self.guiRoot=tk.Tk()
        self.guiRoot.title("Poke Dex Explorer")
        self.guiRoot.geometry("440x640")
        self.guiRoot.resizable(False, False)
        self.guiRoot.configure(bg=backgroundcolor)

        ##title
        tk.Label(self.guiRoot,text="★ Pokemon Explorer ★",font=("Comic Sans MS", 20, "bold"),
                 bg=backgroundcolor,fg=panelcolorlight
                 ).pack(pady=12)
        

        #search background#

        searchbackground= tk.Frame(self.guiRoot,bg=panelcolorlight,bd=4,relief="ridge")
        searchbackground.pack(padx=15,pady=8, fill="x")

        #search title

        tk.Label(searchbackground,text="Enter Pokemon Name/ID",
                 font=("Arial", 11, "bold"),bg=panelcolorlight,fg=darktextcolor1).pack(pady=(6,2))
        
        #search bar

        self.entry=tk.Entry(searchbackground,font=("Arial",13),justify="center",bd=3,
                            relief="sunken")
        self.entry.pack(padx=10,pady=6,fill="x")

        # search button
        tk.Button(searchbackground,text="Search",font=("Arial",11,"bold"),bg=panelcolordarker,
                  fg=innercolor,activebackground=panelcolordark,
                  bd=3,relief="raised",command=self.SearchPokemon).pack(pady=8)
        

        #image box

        self.imagePanel=tk.Frame(self.guiRoot,bg=panelcolorlight,bd=4,relief="ridge")
        self.imageInput=tk.Label(self.imagePanel,bg=panelcolorlight)
        self.imageInput.pack(padx=10,pady=10)
        self.imagePanel.pack_forget()

        #info Frame
        self.infoFrame= tk.Frame(self.guiRoot,bg=backgroundcolorlighter,bd=4,relief="ridge")
        self.infoFrame.pack(padx=15, pady=10,fill="both",expand=True)

        #info scrolbar

        InfoScrollbar=tk.Scrollbar(self.infoFrame)
        InfoScrollbar.pack(side="right",fill="y")

        self.infoOutputs=tk.Text(self.infoFrame,font=("Courier New", 11),bg=backgroundcolorlighter,
                                 fg=innercolor,wrap="word",yscrollcommand=InfoScrollbar.set,bd=0)
        self.infoOutputs.pack(padx=10,pady=10,fill="both",expand=True)
        InfoScrollbar.config(command=self.infoOutputs.yview)

        self.infoOutputs.insert("end", "✨ Welcome to the Pokedex! ✨")
        self.infoOutputs.config(state="disabled")

    def runGui(self):
        self.guiRoot.mainloop()

    def SearchPokemon(self):
        name=self.entry.get().lower().strip()
        if not name:
            messagebox.showwarning("Error","Search Input is blank. Please type a pokemon name.")
            return

 
        url=f"https://pokeapi.co/api/v2/pokemon/{name}"
        urlResponse=requests.get(url)
        print(urlResponse.status_code)
        if urlResponse.status_code == 404:
            messagebox.showerror("Error", "That pokemon name doesn't exist.")
            return
        elif urlResponse.status_code != 200:
            messagebox.showerror("Error", "api error!")
            return

        self.displayPokemon(urlResponse.json())


    def displayPokemon(self,data):
        imageUrl=data["sprites"]["front_default"]
        if imageUrl:
            imageData=requests.get(imageUrl).content
            imageContent=Image.open(io.BytesIO(imageData)).resize((160,160))
            OutputedImage=ImageTk.PhotoImage(imageContent)

            self.imageInput.config(image=OutputedImage)
            self.imageInput.image= OutputedImage

            self.imagePanel.pack(before=self.infoFrame,padx=15,pady=10)
        else:
            self.imageInput.pack_forget()
        
        types = ", ".join(
            type["type"]["name"].capitalize()
            for type in data["types"]
        )

        stats = {}
        for stat in data["stats"]:
            stats[stat["stat"]["name"]] = stat["base_stat"]

        info = (
            f"★ Name: {data['name'].capitalize()}\n"
            f"★ ID: {data['id']}\n"
            f"★ Type(s): {types}\n"
            f"★ Height: {data['height']}\n"
            f"★ Weight: {data['weight']}\n\n"
            f"Stats\n"
            f"HP      : {stats['hp']}\n"
            f"Attack  : {stats['attack']}\n"
            f"Defense : {stats['defense']}\n"
            f"Speed   : {stats['speed']}"
        )

        self.infoOutputs.config(state="normal")
        self.infoOutputs.delete("1.0","end")
        self.infoOutputs.insert("end",info)
        self.infoOutputs.yview_moveto(0)
        self.infoOutputs.config(state="disabled")
    
    



app=CreateGuiApp()
app.runGui()

