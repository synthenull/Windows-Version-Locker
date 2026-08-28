# developed by https://github.com/synthenull

import ctypes
import os
import sys
import winreg

os.system("title Windows Version Locker - github.com/synthenull")
os.system("color e")
os.system("cls")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if not is_admin():
    print('[!] Administrator privileges required. Relaunching as administrator...')
    ctypes.windll.shell32.ShellExecuteW(
        None, 'runas', sys.executable, ' '.join(sys.argv), None, 1
    )
    sys.exit()

print('[+] Administrator privileges confirmed. Starting operations...\n')

target_version = input(
    '[>] Enter the Windows 11 version you want to lock to (e.g., 24H2): '
).strip()

if not target_version:
    print('[-] Invalid version entered. Operation cancelled.')
    input('[!] Press ENTER to exit...')
    sys.exit()

key_path = r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate'

try:
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
        winreg.SetValueEx(key, 'TargetReleaseVersion', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, 'ProductVersion', 0, winreg.REG_SZ, 'Windows 11')
        winreg.SetValueEx(
            key, 'TargetReleaseVersionInfo', 0, winreg.REG_SZ, target_version
        )

    print(
        f'\n [+] Operation completed successfully! Windows 11 locked to version {target_version}.'
    )
    print("[!] Please restart your computer for the changes to take effect.")
except Exception as e:
    print(f"\n[-] Error: {e}")

input('\n [!] Press ENTER to exit...')