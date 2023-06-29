## Virtual environment

Steps:
- add file named `.gitignore` and include `pyladies/` - the name of the venv folder you would like to exclude from repo
- go to repo folder and execute
`python -m venv pyladies`, where `pyladies` is the name of your venv folder
- activate the venv by `Scripts\activate` in `cmd` terminal or `Scripts\Activate.Ps1` in `powershell` terminal
- run command to install required libraries by `pip install -r requirements.txt`