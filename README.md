# Readme

`strong-passphrase` is a simple command line tool written in Python that you can use to randomly generate a strong passphrase.
The tool uses the Python `secrets` library so the random generation should be secure.
We have not made any attempts to scrub the generated password from RAM so if you're worried about some other process getting ahold of it by inspecting memory you should use a different tool.

## Installation

To install the script you will first need to install a version of python after 3.9 and then run the following commands:

```bash
python3 -m pip install pipx
pipx install strong-passphrase
```

You might be wondering "What is `pipx`? Why should I install that?".
`pipx` is a python tool that helps to install python based executables from PyPI.
It installs `strong-passphrase` in it's own virtual environment.
This helps keep dependencies for this tool isolated from other Python tools you might have installed on your system.

## Usage

Simply run `strong-passphrase` and a new randomly generated passphrase will be printed to your terminal.