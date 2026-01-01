import os
import subprocess
import eel

from engine.features import *
from engine.command import*

eel.init("www")
playAssistantSound()
 
   
os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    
eel.start(
    'index.html',
    host='localhost',
    port=8000,  
    mode=None,
    block=True
    ) 
    

