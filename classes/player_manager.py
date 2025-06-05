from functions.utils import clearScreen
class Player:
    def __init__(self, name, starting_bank=1000):
        self.name = name
        self.setup = False
        self.bank = starting_bank
        self.statistics = {
            "games_played": 0,
            "games_won": 0,
            "games_lost": 0,
            "games_tied": 0,
            "total_bet": 0,
            "total_winnings": 0
        }
    def readableStats(self):
        stats = []
        for stat, value in self.statistics.items():
            stats.append(f"{stat.replace('_', ' ').title()}: {value}")
        stats.append(f"Current Balance: {self.bank}")
        
        return "\n".join(stats)
    
    