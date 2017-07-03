import mysql.connector


def get_results():

    conn = mysql.connector.connect(user='cmu', password='!CountMU123',
                                   host='127.0.0.1', database='count_me_up')
    cur = conn.cursor()

    # First intention was to calculate votes with a rank like function
    # Seems to be a bug with mysql storing variables from one row to the next
    # cur.execute("""
    #     Select candidate, count(*)
    #     From (
    #         SELECT candidate,
    #             @vote_rank := IF(@current_voter = voter_id, @vote_rank + 1, 1) AS vote_rank,
    #             @current_voter := voter_id
    #         FROM votes
    #         ORDER BY voter_id, vote_time
    #     ) ranked
    #     where vote_rank <= 3
    #     Group by candidate;
    # """)

    # Get a list of all candidates
    cur.execute("""
    SELECT * From candidates
    """)
    cand_names = []
    cand_votes = {}
    for row in cur.fetchall():
        cand_names.append(row[1])
        cand_votes[row[0]] = 0

    # get an ordered list of all the votes cast and who cast them.
    cur.execute("""
    SELECT candidate, voter_id
    FROM votes
    ORDER BY voter_id, vote_time
    """)

    # count through all votes from the same voter and only count the first 3 made.
    previous_id = -999
    current_num_votes = 0
    for row in cur:
        # print row
        if row[1] == previous_id:
            current_num_votes = current_num_votes + 1
        else:
            current_num_votes = 1
            previous_id = row[1]

        if current_num_votes <= 3:
            cand_votes[row[0]] = cand_votes[row[0]] + 1

    # print cand_names
    # print cand_votes

    # format results into simple string table.
    num = len(cand_names)
    output = ''
    for i in range(0, num):
        output = output + '| '
        output = output + cand_names[i]
        output = output + ' | '
        output = output + str(cand_votes[i+1])
        output = output + ' | \n'

    # print output

    # write results to the file.
    with open('results_table.txt', 'wb') as res_file:
        res_file.write(output)
