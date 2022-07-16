# Pywinauto-Zoom-Automatization
Its a python program, which speeds up the process of joining to meeting and sharing the screen. 

### required packages: 
Pywinauto,
pyautogui,
time,
pynput,
pyserial,
serial

# 16th May. 
### Trying to Add the function to work in background on windows. 
### It's not very optimised code but with time I will update it. 

# 8th June. 
### Added library pynput, which helps to work with inputs. Its adding the posbility to listen for inputs, when the program is minised. This helps a lot, because this script will work with arduino. Arduino will send the keystrokes when the foregin button is clicked, and it will triger the proper function to execute. 
### Also added the function, which close the sharing screen automatically. 

# 16th July. 
### Project released. We changed the way, how to deal with inputs. The arduino is sending the serial signals to the pc. This program connects to this serial and read the lines. If the button is pressed, the signal changes. Programm catches that, and execute a specific function. It is using algorigthim, which compares the state of the line. IF the state changes, so is pressed it goes along and compares still until the button is released. If the stated pressed is compared with state released, then the function is executed. 

Now I will try to make this programm better and create new functions
