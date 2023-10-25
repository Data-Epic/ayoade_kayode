Head to Google Developers Console and create a new project (or select the one you already have).
In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.
Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
Fill out the form
Click “Create” and “Done”.
Press “Manage service accounts” above Service Accounts.
Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.
Select JSON key type and press “Create”.
This will automatically download a json file.
Run touch secret.json in the project directory to create a new file.
Store the content of the downloaded json file in the created file.


To get started with this project, you will need to create a virtual environment and install the following libraries using the command below.

To create a virtual environment with pip, run
run python -m venv .venv
To activate the created environment, run
run source venv/bin/activate on macos on windows, change the bin to scripts
To install the needed libraries run
pip install gspread pandas python-dotenv
change working directory 
cd gspread-workspace