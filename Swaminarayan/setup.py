from setuptools import find_packages
# from setuptools import setup
import sys
from cx_Freeze import Executable, setup

base = None
if sys.platform == "win32":
    base = "Win32GUI"


executables = [Executable('Swaminarayan/Swaminarayan.py',
                          base=base,
                          icon=r"F:\executable-python-windows\Swaminarayan\icon.ico",
                          shortcutName='Swaminarayan',
                          shortcutDir='Desktop')]

setup(
  name='Swaminarayan',
  version='1.0.0',
  description='Swaminarayan description',
  author='Ghanshyam Maharaj',
  url='https://github.com/ajinzrathod/Swaminarayan',
  packages=find_packages(),
  entry_points={
    'console_scripts':[
      'hello-world-cli = Swaminarayan.Swaminarayan:main',
    ],
  },
  executables=executables,
)
# print(a)