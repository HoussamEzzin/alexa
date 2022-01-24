import os

def git_add_all():
    os.system('cmd /c "git add ."')
    
def git_commit():
    os.system('cmd /c "git commit -m "update""')

def git_push():
    os.system('cmd /x "git push"')