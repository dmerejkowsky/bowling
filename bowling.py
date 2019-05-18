class Game:
    def __init__(self):
        self._rolls = [0] * 21
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1


    def is_spare(self, first_in_frame):
            return self._rolls[first_in_frame] + self._rolls[first_in_frame+1] == 10

    def is_strike(self, first_in_frame):
            return self._rolls[first_in_frame] == 10


    def next_two_balls_for_strike(self, first_in_frame):
        return self._rolls[first_in_frame + 1] + self._rolls[first_in_frame + 2]

    def next_ball_for_spare(self, first_in_frame):
        return self._rolls[first_in_frame + 1]

    def two_balls_in_frame(self, first_in_frame):
        return  self._rolls[first_in_frame] + self._rolls[first_in_frame+1]

    def score(self):
        score = 0
        first_in_frame = 0
        for frame in range(10):
            if self.is_strike(first_in_frame):
                score += self.next_two_balls_for_strike(first_in_frame)
                score += 10
                first_in_frame += 1
            elif self.is_spare(first_in_frame):
                score += 10
                score += self.next_ball_for_spare(first_in_frame)
                first_in_frame += 2
            else:
                score += self.two_balls_in_frame(first_in_frame)
                first_in_frame += 2
        return score
