from cx_Freeze import setup, Executable

setup(name = "Doom Editor" ,
      version = "1.0" ,
      description = "Doom Text Editor" ,
      executables = [Executable("main.py")])
