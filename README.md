 Create and activate virtual env
 
 ```powershell
 python -m venv ./.venv;
 .\.venv\Scripts\Activate.ps1
```
- - - 
 Requirements

```powershell
pip install flask
```
- - - 
App setup
```powershell
set FLASK_APP=app.py
set FLASK_ENV=development
```
- - -
Run 
```powershell
flask run --reload --debug
```