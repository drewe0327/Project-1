import csv

def get_csv_file(file):
    with open(file) as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        players = list(player_reader)
    return players


def players_by_experience(players):
    #a list for inexperienced and experienced players_by_experience
    no_exp_players, exp_players = [],[]
    for player in players:
        #if else statement to place players in appropriate group
            no_exp_players.append(player) if player["Soccer Experience"] == "NO" else exp_players.append(player)
    return no_exp_players, exp_players

def get_players(players, team_list):
    index = 0
    """Sorting players inexperienced and
    experienced players into groups"""
    sorted_players = players_by_experience(players)
    #list of players to rerturn
    player_list =[]
    #list of teams
    teams =[]
    #team dictionary
    for key, value in team_list.items():
        teams.append(key)
    #loops through the groups
    for group in sorted_players:

        roster =len(teams)-1
        #loops through players in the group
        for player in group:
            # assign player to a team using index value
            player['Team']= teams[index]
            # add playey to the list
            player_list.append(player)
            """if the index is less than the number of teams
            then increment it by one. Otherwise reset the index"""
            index += 1 if index < roster else -2

    #returns list with players on their appointed teams
    return player_list

#generates the teams
def get_teams(team_list, player_list):
    for player in player_list:
        team = player['Team']
        if team in team_list:
            team_list[team].append(player)

    return team_list

#writes the team.txt file
def teams_text(player_list):
    file = open("teams.txt", 'a')
    #loops through teams
    for team, players in teams.items():
        #writes the team names
        file.write(team + "\n")
        #loops through players info
        for player in players:
            name = player['Name']
            experience = player['Soccer Experience']
            guardian = player['Guardian Name(s)']
            file.write("{},{}, {}\n".format(name, experience, guardian))
        file.write("\n")


if __name__ == "__main__":
    # open file & get players
    imported_players = get_csv_file('soccer_players.csv')

    # team names
    team_list = {
        'Sharks': [],
        'Dragons': [],
        'Raptors': []
    }

    # assign players to teams
    get_players = get_players(imported_players, team_list)

    # populate team lists
    teams = get_teams(team_list, get_players)

    # output file
    teams_text(teams)
