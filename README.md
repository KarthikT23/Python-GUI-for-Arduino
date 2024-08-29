# Python-GUI-for-Arduino
Usage of Python GUI to control Arduino and its sensors, actuators
# Requirements
1) Arduino board (Uno, Nano etc)
2) Arduino IDE
3) VS Code or any other IDE
4) Jumper wires
5) LEDs
6) Pushbuttons
7) Resistors: 10k, 330R

# Software installations
1) Arduino IDE: https://www.arduino.cc/en/software
2) Python: https://www.python.org/downloads/

# Libraries and Modules necessary
1) Firmata library, available in Arduino Library Manager, download from there
2) pyFirmata module: type the installation command "pip install pyFirmata" in the terminal of VS Code


# Important note
If you are using python version above 3.5, then you will have to do a small change in your pyfirmata.py script to avoid  
line 185, in add_cmd_handler

   len_args = len(inspect.getargspec(func)[0])
                       

                       
AttributeError: module 'inspect' has no attribute 'getargspec'. Did you mean: 'getargs'? 

Inside your pyfirmata.py script, go to line 185 and edit len_args = len(inspect.getargspec(func)[0]) to len_args = len(inspect.getfullargspec(func)[0]). Then save the file and run your regular script.



# Reference
https://www.youtube.com/playlist?list=PL09ZAP7_T_Lln5-Is8bsQ28YhYrBgBMn3
