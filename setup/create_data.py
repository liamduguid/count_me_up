# import mysql.connector
from datetime import datetime
import csv
# import os

# originally tried to right straight to sqlite but a bad idea for 10000000 rows
# conn = mysql.connector.connect(user='cmu', password='!CountMU123',
#                                host='127.0.0.1', database='count_me_up')
# cur = conn.cursor()

# open csv file
csv_file = open('sql_data.csv', 'wb')
writer = csv.writer(csv_file, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)

# create all votes
for i in range(1, 10000001):
    # choose candidate
    candidate = ''
    if i <= 500000:
        candidate = 1
    elif i <= 1500000:
        candidate = 2
    elif i <= 3500000:
        candidate = 3
    elif i <= 6000000:
        candidate = 4
    else:
        candidate = 5

    # add voter_id calculation
    voter_id = i
    if i > 500000 and i <= 1500000:
        voter_id = i - 500000
    elif i > 1500000 and i <= 3500000:
        voter_id = i - 1500000
    elif i > 3500000 and i <= 4500000:
        voter_id = i - 3500000
    elif i > 6000000 and i <= 7000000:
        voter_id = i - 6000000

    # write row to file
    values = (i, str(datetime.now()), voter_id, candidate)
    writer.writerow(values)

    # c.execute("""
    #     Insert into results_vote (vote_time, voter_id, candidate_id)
    #     Select ?, ?, id From results_candidates where candidate_name = ?
    # """, values)
    # conn.commit()

csv_file.close()
