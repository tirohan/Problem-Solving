class Football_player:

    def __init__(self, fname, lname, jersy_no):

        self.fname = fname
        self.lname = lname
        self.jersy_no = jersy_no 

P1 = Football_player('Messi', 'Leonel', 10)
P2 = Football_player('Ronaldo', 'Cristiano', 7)
P3 = Football_player('Neymar', 'JR', 10)


print(P1.fname, P1.jersy_no)
print(P2.fname, P2.jersy_no)
print(P3.fname, P3.jersy_no)