# Les règles

Frame -> 2 rolls

roll1 roll2 score
   1    4     5
   4    5    14
   6    4    29    # spare : 10 + next ball
   5    5    49
   10   *    60    # strike: 10 + next 2 balls
   0    1    61
   ...


last frame: if spare -> 1 ball more
            if strike -> 2 more balls


# drawing board

Game               Frame            Roll
roll(pins)   ->              ->     pins
score()
                     ^
                     |
                   TenthFrame


Game contains frames
frames contains rolls
Frame contains link to the next frame

# Test suite

- can create game
- can roll   refactor -> test_create is useless
- test_gutter game -> 20 zeros
- test_all_ones -> 22   # just add all the pins
- dedup test code -> roll many
- all twos -> we know that will pass
- test_one_spare!  5 , 5 , 3 , 17 zeros -> score = 16
- can't make it pass, the design is wrong.
    -> score() does not calculate the score, roll() does!
- back out, put pins in an array (`self._rolls = [0] * 21`, `self._current_roll`, get rid of `self._score`
- back to failing
- use enumerate -> still not ok -> we're not using frames
- iterate through the frames -> big if / else
   refactor: i -> first_in_frame
   comment -> extract self.is_spare()
   tests -> keep in clean too
   let's create a roll_spare -> uh, oh too many function taking `game` as first param
   let's create a GameTest class
 - test_one_strike() 10, 3, 4, 16 zeros -> score = 24
 - refactor()
     is_strike()
     next_two_balls_for_strike
     next_ball_for_spare
     two_ball_in_frame
     roll_strike()

- test_perfect_game()  - wat?

Let's take at the code again -> it **reads** like the rules!
We were going to implement TenthFrame!


