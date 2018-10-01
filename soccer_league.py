""""
You have volunteered to be the Coordinator for your town’s youth soccer league. As part of your job you need to divide the 18 children who have signed up for the league into three even teams - Dragons, Sharks and Raptors. In years past, the teams have been unevenly matched, so this year you are doing your best to fix that. For each child, you will have the following information: Name, height (in inches), whether or not they have played soccer before, and their guardians’ names. You'll take a list of these children, divide them into teams and output a text file listing the three teams and the players on them. There are three main tasks you'll need to complete to get this done:

    In your Python program, read the data from the supplied CSV file. Store that data in an appropriate data type so that it can be used in the next task.

    Create logic that can iterate through all 18 players and assign them to teams such that each team has the same number of players. The number of experienced players on each team should also be the same.

    Finally, the program should output a text file named -- teams.txt -- that contains the league roster listing the team name, and each player on the team including the player's information: name, whether they've played soccer before and their guardians' names.
"""





import csv


# Defining functions
def read_csv(filename):
    with open(filename, newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        player_league = list(player_reader)
    return player_league


if __name__ == "__main__":
    # Reading the CSV file
    player_league = read_csv("soccer_players.csv")

    # Separate experienced and non-experienced players
    experienced_players = []
    not_experienced_players = []
    for row in player_league:
        if row['Soccer Experience'] == 'YES':
            experienced_players.append(row)
        else:
            not_experienced_players.append(row)
    # setting up teams for experienced and not experienced players into teams
    not_experienced_team_1 = not_experienced_players[0:3]
    not_experienced_team_2 = not_experienced_players[3:6]
    not_experienced_team_3 = not_experienced_players[6:9]

    experienced_team_1 = experienced_players[0:3]
    experienced_team_2 = experienced_players[3:6]
    experienced_team_3 = experienced_players[6:9]
    sharks = not_experienced_team_1 + experienced_team_1
    dragons = not_experienced_team_2 + experienced_team_2
    raptors = not_experienced_team_3 + experienced_team_3

    # creating "teams.txt"
    with open("teams.txt", "w") as file:
            file.write("Sharks\n")
            for player in sharks:
                file.write("{Name}, {Soccer Experience}, ""{Guardian Name(s)}\n".format(**player))
            file.write("\nDragons\n")
            for player in dragons:
                file.write("{Name}, {Soccer Experience}, ""{Guardian Name(s)}\n".format(**player))
            file.write("\nRaptors\n")
            for player in raptors:
                file.write("{Name}, {Soccer Experience}, ""{Guardian Name(s)}\n".format(**player))


