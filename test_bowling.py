import bowling

class GameTest(bowling.Game):
    def roll_many(self, count, value):
        for i in range(count):
            self.roll(value)
            
    def roll_spare(self):
        self.roll(5)
        self.roll(5)
        
    def roll_strike(self):
        self.roll(10)

def test_can_create_game():
    game = GameTest()

    
def test_can_roll():
    game = GameTest()
    game.roll(2)
    

def test_gutter_game():
    game = GameTest()
    game.roll_many(20, 0)
    assert game.score() == 0
    

def test_all_ones():
    game = GameTest()
    game.roll_many(20, 1)
    assert game.score() == 20
    
    
def test_one_spare():
    game = GameTest()
    game.roll_spare()
    game.roll(3) 
    game.roll_many(17, 0)
    assert game.score() == 16
    

def test_one_strike():
    game = GameTest()
    game.roll_strike()
    game.roll(3)
    game.roll(4)
    game.roll_many(16, 0)
    assert game.score() == 24
    
def test_perfect_game():
    game = GameTest()
    game.roll_many(20, 10)
    assert game.score() == 300
