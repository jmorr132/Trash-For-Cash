import psycopg2
import bleach

def connect():
    # Connets to the PostgreSQL database. This returns the Database Connection.
    return psycopg2.connect("dbname=tournament")

def delete_matches():
    # removes all match records from the database.
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()

def delete_players():
    # Remove all Players records from the Database.
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()

def count_players():
    #Returns the number of players currently registered.
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM count_players")
    DB.commit()
    player_count = c.fetchall()[0][0]
    DB.close()
    return player_count

def is_even(i):
    return ( i % 2) == 0

def register_player(name):
    # registers name and uses bleach to clean the name of the user.
    clean_name = bleach.clean(name, strip=True)
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (player_name) VALUES (%s)", (clean_name,))
    DB.commit()
    DB.close()

def player_standings():
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM current_standings")
    DB.commit()
    standings = c.fetchall()
    DB.close()
    return standings

def report_match(winner, loser):
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s,%s);",(winner, loser))
    DB.commit()
    DB.close()

def swiss_pairings():
    DB = connect()
    c = DB.cursor()
    match_count = c.execute("SELECT COUNT(*) FROM matches")
    c.execute("SELECT player_id, player_name FROM current_standings")
    standings = c.fetchall()
    DB.commit
    c.execute("SELECT player_id, player_name FROM seed_initial_round")
    seed = c.fetchall()
    DB.commit()

    """ Get player_count from count_players function """
    player_count = count_players()
    """ determine if playercount is an even number """
    if is_even(player_count) == True:
        pairings = []

        """ randomly seed matches if no matches have been played. """
        if match_count == 0:
            for x in range(0, player_count-1, 2):
                pairings.append(seed[x] + seed[x+1])
        else:
            for x in range(0, player_count-1, 2):
                pairings.append(standings[x] + standings[x+1])

    else: raise ValueError("The tournament requires and even number of players. \
                            Please add or remove a single player.")
    """ close the DB and return the match pairings """
    DB.close()
    return pairings