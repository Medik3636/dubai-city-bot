class TapToEarn:
    def __init__(self, user_id):
        self.user_id = user_id
        self.coins = 0
        self.energy = 1000

    def tap(self):
        if self.energy >= 1:
            self.energy -= 1
            self.coins += 1
            return self.coins
        return 0