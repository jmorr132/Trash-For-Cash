-- deletes database if there is one in existance
DROP DATABASE IF EXISTS tournament;
-- creates the tournament database
CREATE DATABASE tournament;
-- connects to the tournament database
\c tournament


-- creates players table
CREATE TABLE players(
    player_id SERIAL PRIMARY KEY,
    player_name TEXT NOT NULL
);

-- creates Matches table
CREATE TABLE matches(
    match_id SERIAL PRIMARY KEY,
    winner INT REFERENCES players (player_id),
    loser INT REFERENCES players (player_id)
);

-- count registered players view
CREATE OR REPLACE VIEW count_players AS
    SELECT COUNT(*) AS reg_players
    FROM players;

-- create the view for player standings
CREATE OR REPLACE VIEW current_standings AS
    SELECT  player_id,
            player_name,
            SUM(CASE WHEN players.player_id = matches.winner THEN 1 ELSE 0 END) AS wins,
            COUNT(matches) AS match_count
    FROM players
    LEFT OUTER JOIN matches
    ON players.player_id = matches.winner OR players.player_id = matches.loser
    GROUP BY player_id
    ORDER BY wins DESC,
             match_count ASC;
             
-- create a view to randomly seed the matches before the first round.
CREATE OR REPLACE VIEW seed_initial_round AS
    SELECT * 
    FROM players
    ORDER BY random();

