from typing import Dict, List


class Player:
    def __init__(self, name):
        self.name = name


class TennisGame1:
    def __init__(self, player1Name: str, player2Name: str):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points: int = 0
        self.p2points: int = 0

    def won_point(self, playerName: str):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        points: Dict[int, str] = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

        if self.p1points == self.p2points:
            if self.p1points >= 3:
                return "Deuce"
            else:
                return f"{points.get(self.p1points)}-All"

        elif self.p1points >= 4 or self.p2points >= 4:
            minusResult = self.p1points - self.p2points
            if minusResult == 1:
                return f"Advantage {self.player1Name}"
            elif minusResult == -1:
                return f"Advantage {self.player2Name}"
            elif minusResult >= 2:
                return f"Win for {self.player1Name}"
            else:
                return f"Win for {self.player2Name}"

        else:
            return f"{points[self.p1points]}-{points[self.p2points]}"


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        self._point_map: Dict[int, str] = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def is_tied(self):
        return (self.p1points == self.p2points) and (self.p1points >= 0)

    def _tied_score(self):
        if self.p1points < 3:
            return f"{self._point_map[self.p1points]}-All"
        else:
            return "Deuce"

    def _has_advantage(self):
        if self.p1points - self.p2points == 1 and self.p1points >= 4:
            return True
        elif self.p2points - self.p1points == 1 and self.p2points >= 4:
            return True

    def _has_win(self):
        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            return True
        elif self.p2points - self.p1points >= 2 and self.p2points >= 4:
            return True

    def rally_score(self):
        return f"{self._point_map[self.p1points]}-{self._point_map[self.p2points]}"

    def player1_in_lead(self):
        return self.p1points > self.p2points

    def player2_in_lead(self):
        return self.p2points > self.p1points

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1

    def score(self):

        if self.is_tied():
            return self._tied_score()

        if self.player1_in_lead():
            if self._has_win():
                return "Win for " + self.player1Name
            if self._has_advantage():
                return "Advantage " + self.player1Name

        if self.player2_in_lead():
            if self._has_win():
                return "Win for " + self.player2Name
            if self._has_advantage():
                return "Advantage " + self.player2Name

        return self.rally_score()


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return (
                "Advantage " + s
                if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1)
                else "Win for " + s
            )
