# Distilled_SCH

Desmond Fitzgerald  
Technical challeenge for Distilled SCH  

## Data Clensing

Before loading the data the .csv file was cleaned.  
Duplicate id fixed.  
Blank spaces were removed
Quote marks on price were changes.  
Date fromat was standarized.  

### File Names

*dataset.cvs - This is .csv file to be imported into the database table.
*curl.sh     - This is a bash file with the curl commands.
*app.py      - This is the app python code.

### Procedure

*Open an interactive python shell and run 'python app.py'
*Open a command prompt in which to run the curl commands (see curl.sh) - The results of each curl command are returned.
*Open a browser and navigate to localhost:5000/car - the details for all cars are displayed on the webpage
*Navigate to localhost:5000/car/1  - The details of the car with id 1 is displayed on the webpage. changing the id will change the details.

### Testing
*Database creation and loading was tested using DB Browser for SQLite. This confirmed that the table was created and correct data was loaded.
*Connection to the database was tested using curl command.
*Webpage updating was confirmed at each step in the process.
