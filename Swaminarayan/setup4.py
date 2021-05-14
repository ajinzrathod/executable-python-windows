import sys
from cx_Freeze import setup, Executable


# https://stackoverflow.com/questions/15734703/use-cx-freeze-to-create-an-msi-that-adds-a-shortcut-to-the-desktop

# shortcut_table = [
#     ("DesktopShortcut",        # Shortcut
#      "DesktopFolder",          # Directory_
#      "Swaminarayan",           # Name
#      None,                     # Component_
#      None, 
#      None,                     # Arguments
#      None,                     # Description
#      None,                     # Hotkey
#      None,                     # Icon
#      None,                     # IconIndex
#      None,                     # ShowCmd
#      'TARGETDIR'               # WkDir
#     )]

# msi_data = {"Shortcut": shortcut_table}
# bdist_msi_options = {'data': msi_data}

# Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options = {"packages": ["os"], "excludes": []}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"



setup(
    name = "Swaminarayan",
    url='https://github.com/ajinzrathod/Swaminarayan',
    version = "0.1",
    description = "My GUI application!",
    options = {
        "build_exe": build_exe_options,
        "bdist_msi": {
            'install_icon': r"F:\executable-python-windows\Swaminarayan\icon.ico", 
            }
        },
    executables = [
    	Executable("Swaminarayan/Swaminarayan.py",
    		 base=base,
    		 icon=r"F:\executable-python-windows\Swaminarayan\icon.ico",
    		 shortcutName='Swaminarayan',
    		 shortcutDir='DesktopFolder',
    		 )
    	]
    )