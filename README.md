#count me up

A simple application counting the votes distributed to candidates.


**Setup**

clean installations of the following programs and packages

- MySQL
- python2.7
- mysql-connector-python

setup mysql:

run: 
`/setup/setup_db.sh count_me_up cmu '!CountMU123'`
- will ask for the the mysql root password

run: 
`python create_data.py`
- this creates the 10000000 row dataset for the test.

run: 
All of the sql scripts found in `setup_tables.sql`
- This will create the tables needed and populate them with the data.

run the site:

`python -m SimpleHTTPServer`
- This starts the http server. Have to be sure nothing else is running on port 8000.

`python run_backend.py`
- This runs the results calculation.

**Process**

- I stared with a simple html page that updated every second and grabbed data from a local file with an Ajax request.
- I then concentrated on setting up the MySQL database to house the data and write the scripts to create the sample data.
- The size of the data set started to cause problems here and I found the easiest way with my set up was to write the data
to a csv file and then import this into MySQL.
- I reduced the data size to build the rest.

- I then worked on the SQL scripts to aggregate the results of the voting.
- This is where i hit a issue with the tool I chose. Simple aggregation of all the data can be done calling MySQL from 
python but the detail of each voter only being able to vote 3 times calls for functionality such as rank and partition 
which are not features of MySQL.
- I wrote a script to imitate the rank function but seem to hit a bug when running from python. While calling MySQL from 
python I do not seem to be able to define variables that persists to the next row of the table. 
- I eventually decided to calculate the votes in python which is much slower but correct.

**Optimise**

I did not have time to look at this but if I was to do it again I would start differently.

- I would try to use a different database solution such as PostgreSQL which provides some more powerful aggregation 
functionality.

- I would also look at splitting up the job of counting the votes between processes to speed it up. 

- Lastly I would improve upon how the html page grabs the results from the python script.