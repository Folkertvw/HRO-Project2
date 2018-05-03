import psycopg2


# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=SudokuScore user=quinten")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results


# Uploads a score into the hiscore table
def upload_score(name, Game_Win):
    interact_with_database("UPDATE score SET Game_Win = {} WHERE name = '{}'"
                           .format(Game_Win, name))


# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM score")


# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM score ORDER BY Game_Win")[0][1]
    return result

# in pgAdmin maak een database genaamd score
# maak een table create table score(
#    name varchar(30),
 #   Game_Win int
  #  )