import os
import subprocess
import eel

from engine.__pycache__.features import *
from engine.__pycache__.command import*

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
    

