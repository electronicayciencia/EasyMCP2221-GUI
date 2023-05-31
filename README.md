# EasyMCP2221 Workbench
Graphical User Interface for EasyMCP2221 library.

EasyMCP2221 Workbench is a tkinter GUI to experiment with MCP2221 and MCP2221A chips. 
It is based on [EasyMCP2221 library](https://github.com/electronicayciencia/EasyMCP2221).

See full documentation on [easymcp2221.readthedocs.io](https://easymcp2221.readthedocs.io).

## Run

### Windows

Download pre-compiled binaries or run from source.

### From source

Clone the repository and install requirements.

    cd workbench
    python EasyMCP2221-workbench.pyw
    
To hide console, double click on `EasyMCP2221-workbench.pyw` or use:

    pythonw EasyMCP2221-workbench.pyw


### Linux

    sudo apt-get install python3-tk
    pip install -r requirements.txt

## High DPI

To solve blurry fonts on high DPI screens (at the expense of tiny characters) use:

    EasyMCP2221-workbench.exe --highdpi


## Misc

### Compile

To compile:

    pyinstaller EasyMCP2221-workbench.spec


Note *pyinstaller-action-windows* requires spec file with the sources.

Command line to regenerate spec file:

    pyinstaller \
      --onefile \
      -w \
      --icon=assets/icon.ico \
      --add-data="assets/icon.ico;assets" \
      --add-data="assets/icon.png;assets" \
      -n "EasyMCP2221-workbench" \
      EasyMCP2221-workbench.pyw


