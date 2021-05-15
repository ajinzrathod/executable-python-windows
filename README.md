#  Make a Python Script as Microsoft Windows Installer

See how to name the version number for your GitHub code at [semver](https://semver.org/)

## Write a short code
* Create a folder **myapp**


* Create a file in **myapp** directory named *main.py*
(You could name it anything other than `main.py`).
 
* Open `main.py` and paste the following code.

```python
import tkinter as Tkinter


def main():
	top = Tkinter.Tk()
	top.geometry("500x500")
	B = Tkinter.Button(top, text ="Ghanshyam Maharaj")
	B.pack()
	top.mainloop()

if __name__ == '__main__':
	main()
```

## Create a virtual environment
* Open cmd in **myapp** directory and type 
```bat
py -m venv env
```
*env* is the name of the Virtual Environment. If you see `(env) path/to/myapp`, it means that virtual env is activated successfully.


## Test the Virtual Environment
```bat
.\env\Scripts\activate  
```
If you see `(env)`, it indicataes virtual environment is activated succesfully.

## Test the code
```bat
py main.py
```
This will display a small GUI application that says **Ghanshyam Maharaj**


## Install cx_Freeze

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cx_Freeze.

```bash
pip install cx_Freeze
```
Check [here](https://cx-freeze.readthedocs.io/en/latest/#welcome-to-cx-freeze-s-documentation) if *cx_freeze* is compatible with the *python* version you are using else it will throw some errors.

## Create setup.py file in <myapp> directory
You could name it anything. Copy the follwing code

```python3
import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options = {"packages": ["os"], "excludes": []}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Ghanshyam",
    url='<url to your github code>',  # Not necessary
    version = "1.0.0",  # [Learn how to specify verion number at https://semver.org/
    description = "My GUI application which displays Ghanshyam Maharaj",
    options = {
        # https://cx-freeze.readthedocs.io/en/latest/distutils.html#build-exe
        "build_exe": build_exe_options,

        # bdist_msi: https://cx-freeze.readthedocs.io/en/latest/distutils.html#bdist-msi
        "bdist_msi": {
            # if install_icon is not mentioned here, control panel wont show any icon add/remove programs
            'install_icon': r"<path\to\icon\file\icon.ico>",  # Must be .ico only
            }
        },
    executables = [
    	Executable("main.py",
    		 base=base,
    		 icon=r"<path\to\icon\file\icon.ico>",  # Must be .ico only,
    		 shortcutName='Ghanshyam Maharaj',
    		 shortcutDir='DesktopFolder',
    		 )
    	]
    )
```
> Change all fields with <> as per your configuration

We will Not exclude *tkinter* as our *main.py* is built in *tkinter module*

If you exclude the tkinter module, it will throw error as
```
tkinter not found
```

## Create a Portable Application

Open cmd in *myapp* directory where *setup.py* file is also stored and type

```bat
py setup.py build
```
### If you recieve an error like this:

> **SystemError: <built-in function AddIcon> returned NULL without setting an error**

It means your icon file is missing or path to icon file is incorrect.

### If everything goes well
It will take a while and after the process is completed you will see a folder named *build* in your directory where you will have a folder named **exe.win-\<architecture>-\<python-verion>**.

Open that folder and you will find **main.exe**

Now, you can share this **build** folder with anyone and they can use this script when they will execute **main.exe**

## Create a Executable Installer

If you don't want to provide an entire folder and just an installer, you can use this process.

```
py setup.py bdist_msi
```

There are many tools like *setuptools* which creates an installer, but it will create installer in `C:/Programs/` which requires administrator access.

Using cx_freeze has a great advantage. The application is installed in `AppData` folder and thus no admin permissions are required for normal installation.

It may take few minutes. But after it is completed. You will find a folder named *dist*. Open it and here is your installer. Share this installer with anyone you want to share your application.

If you want to edit the icon at top left corner of our application, it can be done using tkinter. See [here](https://stackoverflow.com/questions/23773825/how-can-change-the-logo-of-tkinter-gui-screen/23773857) how to change icon

After installing, you will find
* Short cut in desktop named Ghanshyam Maharaj
* You can find your application using the windows search bar
* In control panel, you can find your application named **Ghanshyam** under *Program and Features*.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


## References
[cx_freeze | Docs](https://cx-freeze.readthedocs.io/en/latest/)

[cx_freeze | GitHub](https://github.com/marcelotduarte/cx_Freeze)

[Stackoverflow | Use cx-freeze to create a msi that adds a shortcut to the desktop](https://stackoverflow.com/questions/15734703/use-cx-freeze-to-create-an-msi-that-adds-a-shortcut-to-the-desktop)

[cx_freeze | distutils setup script](https://cx-freeze.readthedocs.io/en/latest/distutils.html)

[Youtube | How to Create An .exe And Installer For Python Application using cx_Freeze Module in HINDI | Urdu](https://youtu.be/inuzQfxTOkg)
