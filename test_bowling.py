import bowling

def test_can_create_game():
    game = bowling.Game()


def test_can_roll():
    game = bowling.Game()
    game.roll(0)


def test_can_score():
    game = bowling.Game()
    game.roll(0)
    game.score()
