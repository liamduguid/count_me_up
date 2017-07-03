

Create Table candidates (
id              int Not NULL,
candidate_name  VARCHAR(15),
Primary Key (id)
);


Insert into candidates
Values (1, 'candidate-1');
Insert into candidates
Values (2, 'candidate-2');
Insert into candidates
Values (3, 'candidate-3');
Insert into candidates
Values (4, 'candidate-4');
Insert into candidates
Values (5, 'candidate-5');


Create Table votes (
id          int Not NULL,
vote_time   datetime Not NULL,
voter_id    int Not NULL,
candidate   int Not NULL,
Primary Key (id),
Index vote (voter_id,vote_time)
);


LOAD DATA LOW_PRIORITY LOCAL
INFILE 'sql_data.csv'
INTO TABLE votes
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';