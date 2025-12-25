import os
import subprocess
import eel

eel.init("www")

os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    
eel.start(
    'index.html',
    host='localhost',
    port=8000,
    mode=None,
    block=True
    ) 
    