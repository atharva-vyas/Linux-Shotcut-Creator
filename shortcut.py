import os

# /opt/Idea/bin/idea.sh
execPath = input('Enter the full path to your .sh script that launches the application: ')
# Intellij Idea
name = input('Enter the name of your application: ')
# /opt/Idea/bin/idea.svg
icon = input('Enter the full path to the image that you want to use as icon: ')

print('\nApplication Name:', name)
print('.sh Script Path:', execPath)
print('Application Icon:', icon)

input('\npress any key to confirm...')

os.chdir('/usr/share/applications')
payload = "[Desktop Entry]\nVersion=1.0\nName=" + name + "\nType=Application\nIcon=" + icon + "\nExec=" + execPath

f = open(name.replace(' ', '-') + '.desktop', "a")
f.write(payload)
f.close()