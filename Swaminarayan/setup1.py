import sys
from cx_Freeze import setup, Executable
import os

# One liner
# setup(executables=[Executable("Swaminarayan.py")])


PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
# os.environ['TCL_LIBRARY'] = os.path.join(
    # PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
# os.environ['TCL_LIBRARY'] = os.path.join(
    # PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                  # os.path.join('lib', 'tk86.dll')),
                 # (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                  # os.path.join('lib', 'tcl86.dll'))]

# build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options = {}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable('Swaminarayan/Swaminarayan.py',
                          base=base,
                          icon=r"F:\executable-python-windows\Swaminarayan\icon.ico",
                          shortcutName='Swaminarayan',
                          shortcutDir='Desktop')]

setup(name="Swaminarayan Installer",
      version='1.0',
      author="Lord Swaminarayan",
      description='Lord Swaminarayan Description',
      options={
          'build_exe': {
              'include_files': build_exe_options
               }
      },
      executables=executables)