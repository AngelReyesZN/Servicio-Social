# Create an Executable for your OS from this Repo!
1. Install python version different from Anaconda. We recommend 3.10. Also download UPX for your OS from [here](https://github.com/upx/upx/releases/tag/v4.2.4) and unzip it 
2. Using create a Python virtual environment as follows (**don't use Anaconda or any other environment!**):

    2.1. Create a folder in your preferred path. Example : `D:\> mkdir vEnv`
    
    2.2. Change to that folder and then execute: `D:\vEnv> python -m venv vEnv`
    
    2.3. Search for the Script folder and execute the command based on your OS: `D:\vEnv\vEnv\Scripts> activate.bat`
    | Shell | Command to activate virtual environment |
    | ----- | --------------------------------------- |
    | POSIX || |
    | bash/zsh | $ source <venv>/bin/activate |
    | fish | $ source <venv>/bin/activate.fish |
    | csh/tcsh | $ source <venv>/bin/activate.csh |
    | PowerShell | $ <venv>/bin/Activate.ps1 |
    | Windows || |
    | cmd.exe | C:\> <venv>\Scripts\activate.bat |
    | PowerShell | PS C:\> <venv>\Scripts\Activate.ps1 |

    Now your venv is active! **Don't close the CLI**

3. Clone this repo in another folder
4. On the same instance of the CLI open the folder repo and execute: `D:\Servicio-Social> python -m pip install requirements.txt`
5. Finally execute the command replacing \<this\>:
    
    For CLI only: `pyinstaller --onefile --upx-dir <path to your upx.exe> --clean --name <name of the app> --icon assets\iconcd.ico main.py`
    
    For GUI: `pyinstaller --onefile --windowed --upx-dir <path to your upx.exe> --clean --name <name of the app> --icon assets\iconcd.ico gui.py`

6. Your app will be in the `dist` folder!

For closing the venv execute `deactivate`.

You can delete both folders now.