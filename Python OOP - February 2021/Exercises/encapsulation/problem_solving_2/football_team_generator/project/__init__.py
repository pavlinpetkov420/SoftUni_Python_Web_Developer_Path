from problem_solving_2.football_team_generator.project.player import Player
from problem_solving_2.football_team_generator.project.team import Team

p1 = Player('Johny Sins-Sing', 13, 15.5, 39, 7, 122)
p2 = Player('Johny Sins-Sang', 19, 142.5, 39, 7, 122)
p3 = Player('Johny Sins-Sung', 166, 35.5, 49, 6, 122)
p4 = Player('Johny Sins-Song', 17, 19.5, 18, 4, 122)
p5 = Player('Johny Sins-Sooung', 19, 12.5, 123, 10, 11232)

team = Team('TheProfessionals', 159.8)
print(team.add_player(p1))
print(team.add_player(p2))
print(team.add_player(p3))
print(team.add_player(p4))
print(team.add_player(p5))

print(team.remove_player(p2))
print(team.remove_player(p5))



