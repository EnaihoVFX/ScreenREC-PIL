import customtkinter as ctk
import screenrec

j=0
modes= ["Desktop Record", "Gaming Record", "Window Record", "HD Record", "Lightweight Record", "Custom Record"]

root= ctk.CTk()
root.geometry("820x500")
root.title("Screen Capture")

def main(modes):
    j=0

    mainframe=ctk.CTkFrame(root, width=300, height=505)
    mainframe.pack_propagate(False)
    mainframe.pack(side="left", padx="10")

    buttongrid=ctk.CTkFrame(mainframe, width= 280, height=450)
    buttongrid.grid_propagate(False)
    buttongrid.grid(row=0, column=0)
    
    title= ctk.CTkLabel(mainframe,text="Screen Capture",font=("Arial",20))
    title.grid()

    def chooser(mode):
        if mode==0:
            print("mode")
        if mode==1:
            print(mode)
        if mode==2:
            print(mode)
        if mode==3:
            print("HI")
        if mode==4:
            print(mode)
        if mode==5:
            print(mode)

    for i in modes: 
        recmodes= ctk.CTkButton(buttongrid, text=i, width=130, height=130, command=lambda ch=j: chooser(ch))
        recmodes.grid(row=j//2,column=j%2, padx=5,pady=5)
        j=j+1

    previewframe=ctk.CTkFrame(root, width=480, height=270)
    previewframe.pack_propagate(False)
    previewframe.pack(side="top", padx="5",pady="10")
    
    # setting output widgets

    settingoutputframe=ctk.CTkFrame(root)
    settingoutputframe.pack_propagate(False)
    settingoutputframe.pack()

    resolutionsetting=ctk.CTkLabel(settingoutputframe,text="Resolution: 1080p")
    resolutionsetting.grid(row=0,column=0)

    formatsetting=ctk.CTkLabel(settingoutputframe,text="Format: mp4")
    formatsetting.grid(row=0,column=1)

    codecsetting=ctk.CTkLabel(settingoutputframe,text="Codec: hvec")
    codecsetting.grid(row=1,column=0)

    foldersetting=ctk.CTkLabel(settingoutputframe,text="Folder Path: .../Desktop")
    foldersetting.grid(row=1,column=1)

    #record/screenshot buttons

    buttonframe=ctk.CTkFrame(root)
    buttonframe.pack()

    recordbtn=ctk.CTkButton(buttonframe, text="Record", command=screenrec.start_recording)
    recordbtn.grid(row=0,column=0)
    
    pausebtn=ctk.CTkButton(buttonframe,text="Pause")
    pausebtn.grid(row=0,column=1)

    stopbtn=ctk.CTkButton(buttonframe,text="Stop", command=screenrec.stop_recording)
    stopbtn.grid(row=0,column=2)

    screenshotbtn=ctk.CTkButton(buttonframe, text="Screenshot", command=screenrec.take_screenshot)
    screenshotbtn.grid(row=1,column=1)

    settingsbtn=ctk.CTkButton(buttonframe, text="Settings")
    settingsbtn.grid(row=1,column=2)

    settingsframe=ctk.CTkFrame(root, width=480, height=235)
    settingsframe.pack_propagate(False)
    settingsframe.pack(side="bottom", padx="5",pady="10")

    #resolution option elements

    res_option=ctk.StringVar()
    res_text=ctk.CTkLabel(settingsframe,text="Resolution")
    res_text.grid(row=0,column=0)
    resinput=ctk.CTkOptionMenu(settingsframe, values=["1080p","720p","480p","360p","Display Res","Custom"],variable=res_option)
    resinput.set("Display Res")
    resinput.grid(row=0,column=1)
    
    #format option widget

    format_option=ctk.StringVar()
    formattext=ctk.CTkLabel(settingsframe,text="Format")
    formattext.grid(row=0,column=2)
    formatinput=ctk.CTkOptionMenu(settingsframe, values=["mp4","gif","mov","webp"],variable=format_option)
    formatinput.set("mp4")
    formatinput.grid(row=0,column=3)

    #codec option widget

    codec_option=ctk.StringVar()
    codectext=ctk.CTkLabel(settingsframe,text="Codec")
    codectext.grid(row=1,column=0)
    codecinput=ctk.CTkOptionMenu(settingsframe, values=["hvec","hv1","mpeg","h.264"],variable=codec_option)
    codecinput.set("hvec")
    codecinput.grid(row=1,column=1)

    #folder option widget

    folder_option=ctk.StringVar()
    foldertext=ctk.CTkLabel(settingsframe,text="Folder")
    foldertext.grid(row=1,column=2)
    folderinput=ctk.CTkEntry(settingsframe,textvariable=folder_option,placeholder_text=".../Desktop")
    folderinput.grid(row=1,column=3)
    folderbutton=ctk.CTkButton(settingsframe,text="📂", command=lambda x: print(x=10),width=2)
    folderbutton.grid(row=1,column=4)
    

main(modes)

root.mainloop()