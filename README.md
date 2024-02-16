# hyperdeck-automation
Trigger simultaneously REC/PLAY/STOP commands on multiple Blackmagic Hyperdeck 

When you cannot insert timecode in your videos, it is very handy to be able to start the recordings simultaneously.
We can achieve this by using semaphore and asyncio in Python.

# Usage: 
Modify the IP addresses of your Blackmagic Hyperdecks and modify the Semaphore(x) value accordingly then launch in cmd with:
python REC.py

# Note:
If you want to create an .exe out of this, use a command such as 'pyinstaller --onefile your_script.py'

# Limitation:
The hyperdeck have a strange behaviour : if the PLAY button was pressed before launching the RECORD command, the REC does NOT start, 
it has to be triggered twice. Yet, the server replies '200 OK' as usual even if it does not start recording. 
As it is not possible to know beforehand if PLAY was pressed, the only workaround is to check if all the recorders have started. 
If not, use the STOP command and trigger the REC command a second time and it will always work.



