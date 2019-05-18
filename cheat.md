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


```drawing board

Game               Frame            Roll
roll(pins)   ->              ->     pins
score()
                     ^
                     |
                   TenthFrame


Game contains frames
frames contains rolls
Frame contains link to the next frame


```python
import bo


```
