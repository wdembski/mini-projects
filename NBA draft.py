# -*- coding: utf-8 -*-
"""
This is to simulate the NBA Lottery.  
This link explains the general idea and I copied it's rules here
http://www.tankathon.com/pick_odds

1	All teams missing the playoffs are in the Lottery
2	Teams with worse records get more chances at winning a top four pick (more ping pong ball combos)
3	The 1st overall pick is awarded by a drawing of ping pong balls
4	The 2nd overall pick is awarded by a drawing of ping pong balls
5	The 3rd overall pick is awarded by a drawing of ping pong balls
6	The 4th overall pick is awarded by a drawing of ping pong balls
7	Remaining lottery teams, sorted by record, fill out picks 5-14
8	Playoff teams, sorted by record, are assigned picks 15-30 - playoff seeds and outcomes have no impact
9	Random drawing decides who picks first between teams with same record
10	Tied lottery teams split their ping pong balls evenly, and any odd remainder and the better draft order position are given to the random drawing winner
11	Second round is ordered by record without playoff consideration
12	Second round ties are in reverse order of the teams' first round picks

This can easily be done on new years.  Simply replace values in the correct order
for both lottery_teams and teams_list
"""

import random
full_list = [] # this will hold 1000 values 0-13.  These represent the index of the team below

#all the teams that missed the playoffs in order of worst to best record
lottery_teams = ['Golden State', 'Cleveland', 'Minnesota', 'Atlanta', 'Detroit',
              'New York', 'Chicago', 'Charlotte', 'Washington', 'Phoenix', 
              'San Antonio', 'Sacramento', 'New Orleans', 'Memphis']

#all teams in order of worst to best record
teams_list = ['Golden State', 'Cleveland', 'Minnesota', 'Atlanta', 'Detroit',
              'New York', 'Chicago', 'Charlotte', 'Washington', 'New Orleans',  
              'Sacramento', 'San Antonio', 'Orlando', 'Phoenix', 'Memphis',
              'Portland', 'Brooklyn', 'Dallas', 'Philadelphia', 'Miami', 'Utah',
              'Oklahoma City', 'Houston', 'Indiana', 'Denver', 'Boston', 'LAC',
              'LAL', 'Toronto', 'Milwaukee']

#will contain the teams in the order of their pick
picked_teams = []

lotteryOrder_to_percentage = {1: 14.0, 2: 14.0, 3: 14.0, 4: 12.5, 5: 10.5, 
                             6: 9.0, 7: 7.5, 8: 6.0, 9: 4.5, 10: 3.0, 11: 2.0, 
                             12: 1.5, 13: 1.0, 14: 0.5}

#fill list of possible choices
for order in lotteryOrder_to_percentage:
    picks = int(10 * lotteryOrder_to_percentage[order])
    for j in range(picks):
        full_list.append(order - 1)  

#perform first 4 picks
for pick in range(4):
    try_again = True
    while try_again:
        team = lottery_teams[random.choice(full_list)]
        if team not in picked_teams:
            picked_teams.append(team)
            try_again = False

#fill 5-14 with lottery teams
for team in lottery_teams:
    if team not in picked_teams:
        picked_teams.append(team)

#final 16 picks
for team in teams_list:
    if team not in picked_teams:
        picked_teams.append(team)

for pick, team in enumerate(picked_teams):
    print('#{} pick: {}'.format(pick + 1, team))
    
    
    
    
    
    
    
    

