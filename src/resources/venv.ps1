param ($py_ver)

py $py_ver -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
