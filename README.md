# ScreenREC-PIL
Screen Record Software, Lightweight Python Screen Recording Tool for low resource availability devices

Uses PIL, OpenCV, and CustomTkinter (GUI) to record the screen of a device with low resource demand.

Explanation of Backend

In the ScreenRec.py file most operations are performed, the only main logic i left in the main.py is the unfinished choser case switch that will change the options based on presets that are on the side of the screen when they are clicked.

The ScreenRec file contains the start_recording function which runs by grabbing a screenshot of a set frame size (the users screen but in 1080x1920). This screenshot is one of the many frames which are then written into the video writer. At the end of this loop, the video writer is released and the images are deleted from the computer temp-mem.

Flowchart describing the data flow and how the backend works:

![image](https://github.com/user-attachments/assets/1aaef2bb-2199-40c2-84d8-57f489d10e86)


Future Updates/Plans:
- Fixing the codec option
- Fixing the folder output to append to os, (create a window to popup allowing you to folder search)
- Make the window actually show the ouput preview, option to disable when the mouse hovers the frame
- Improve the GUI and make it look more appealing, possibly implement self made GUI module (will publicly release at a later date)
- Create an FPS option
- Make recording have more advanced options such as the ability to chose specific areas to record in
- Possible gaming feature similar to applications like Powder where the user can enable a gaming clip feature, will use ML to determine which to clip
- Create a custom image grab system similar to PIL imagegrab but with custom codec, will allow me to compress and perserve image quality and later extract and export image files into a video after recording is over, this would further improve performance of the software and its recording system

- Some GUI Previews for those looking to download and test in its early stages:

  ![image](https://github.com/user-attachments/assets/572632d4-6d4a-42a2-8157-df5bad46a646)
  

