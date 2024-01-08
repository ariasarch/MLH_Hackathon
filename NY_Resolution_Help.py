import time
import subprocess

def reminder():
    title = 'Coding Reminder'
    message = 'Time to Code'
        
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    subprocess.run(command, shell=True)

interval = 86400

print("Reminder set! You'll be notified to code every 24 hours.")

while True:
    reminder()
    time.sleep(interval)