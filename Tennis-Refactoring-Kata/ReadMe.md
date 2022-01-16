## General Notes

1. Adding in typing for improved readability
2. The attempts in `first_try.py` were done without the application of the solutions provided by code smells to see what my first responses would be. I will be adding a `second_try.py` file after going over the code smells with my partner.

### Problem 1
I did this one late at night and forgot to write some quality notes, but on the second try I will have some greater detail on my thinking and approach.

### Problem 2
Initial thoughts:
    - The score method is quite bulky with repetive scoring measures. This can be compacted down as in the first problem by creating a points dictionary for quick access.
    - There are a ton of if blocks that each specify a unique condition, I suspect these can be reduced to make the code more reader friendly.
    - Internal accessor methods need to be noted as such by adding a _ in front. (These break the tests, so leave them for now.)
    - `P1res` and `P2res` seem oddly out of place to me, it's also not clear what they represent just from reading the code.
    - The four new method calls are not used at all, so maybe we can make them more impactful.

I will reference each if block to see if I can understand what the authors are intending to accomplish.
    1. `self.p1points == self.p2points and self.p1points < 3` indicates that at most the game is tied at Thirty-Thirty.
    2. `self.p1points == self.p2points and self.p1points > 2` indicates that at least the game is tied at Forty-Forty.
    3. `self.p1points > 0 and self.p2points == 0` indicates that player 1 has scored, but player 2 has not; `P1res` and `P2res` now being used to track scores. 
    4. `self.p2points > 0 and self.p1points == 0` indicates the same as block 3, just for player 2
    5. `self.p1points > self.p2points and self.p1points < 4` indicates the game is not at Deuce yet, but player 1 is ahead of player 2.
    6. `self.p2points > self.p1points and self.p2points < 4` indicates the same as block 5, just for player 2.
    7. `self.p1points > self.p2points and self.p2points >= 3` indicates that the score is at least Advantage-40 for player 1
    8. `self.p2points > self.p1points and self.p1points >= 3` indicates the same as block 7, just for player 2.
    9.  ... remaining code blocks specify logic for the wins, straight forward enough. 

- `SetP1Score` and `SetP2Score` seem unused, and their logic can be just compressed into the `P1Score` and `P2Score` methods instead.
- Block 1 and 2 together cover the spectrum of all scenarios in which the game can be tied, so we can reduce the if block here and not hard code the result.
    - Made this more succint and still 

Overall I feel as if the logic could be separated a bit more into their own method calls. For example, the `_has_advantage()` method is still somewhat ambiguous in that it's not clear who has the advantage. Additionally, the `_tied_score()` method
has a flaw in the logic where it will return the incorrect score. However, this method is only intended to be used internally as well, but I think it could be improved.

### Problem 3
Haven't completed this problem yet.