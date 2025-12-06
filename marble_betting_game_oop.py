import random 

class Player:
    def __init__(self, name, gold, games_played=0, games_won=0):
        self.name = name
        self.gold = gold
        self.original_gold_balance = gold
        self.games_played = games_played
        self.games_won = games_won

    def round_count(self):
        while True:
            try:
                rounds = int(input("How many rounds would you like to play? : "))
                if rounds < 1:
                    print("❌ Invalid input! Please enter 1 or more rounds.")
                    continue 
                self.rounds = rounds
                break
            except ValueError:
                print("❌ Invalid input! Please enter a whole number (e.g., 5).")

    def make_bet(self, bet_amount):
        if bet_amount <= 0:
            print("🚫 Invalid bet amount! Enter 1 or more gold.")
            return False
        elif bet_amount > self.gold:
            print(f"💰 Insufficient balance! You currently have {self.gold} gold.")
            return False
        return True
     
class MarbleGame:
    def __init__(self, marble_bag=None):
        if marble_bag is None:
            marble_bag = ["green", "green", "green", "green", "green", 
                          "white", "black", "red", "red", "red"]
        self.marble_bag = marble_bag

    def run_round(self, player):

        print(f"Gold Balance : {player.gold}")
        player.round_count()
        
        i = 0
        while i < player.rounds:
            i+=1
            print("+-------------------------------------------------------------+")
            print(f"Round : {i} of {player.rounds}")
            while True:
                try:
                    bet_amount = int(input("How much do you want to bet : "))
                    if player.make_bet(bet_amount):
                        break
                    
                except ValueError:
                    print("❌ Invalid input! Please enter a whole number for your bet.")

            chosen_marble = random.choice(self.marble_bag)
            print(f"Marble drawn: {chosen_marble.title()}")
            
            if chosen_marble == 'green':
                print(f"Marble Color : Green - Congratulations! You won ({bet_amount} gold) ✅")
                player.gold += bet_amount
                player.games_won +=1
                
            elif chosen_marble == 'black':
                print(f"Marble Color : 10x Black Marble - Jackpot! You won ({bet_amount * 10} gold) 🏆")
                player.gold += (bet_amount * 10)
                player.games_won +=1
                
            elif chosen_marble == 'white':
                print(f"Marble Color : 5x White Marble - Unlucky! You lose ({bet_amount * 5}) 💩")
                player.gold -= (bet_amount * 5)
                
            elif chosen_marble == 'red':
                print(f"Marble Color : Red - Oops! You lose ({bet_amount}) ❌")
                player.gold -= bet_amount

            player.games_played += 1

            print(f"Current Gold Balance : {player.gold}")

            if player.gold <= player.original_gold_balance / 2:
                print("+------------------------ GAME OVER! -------------------------+")
                print(f"You ran out of luck and finished the game with only {player.gold} gold.")
                break


        profit = player.gold - player.original_gold_balance
        if profit > 0:
            print(f"\n✨ CONGRATULATIONS! You completed all {player.rounds} rounds with a profit of {profit} gold.")
        elif profit < 0:
            print(f"\n😔 You completed all {player.rounds} rounds, finishing with a loss of {profit} gold.")
        else:
            print(f"\n🤝 You broke even after {player.rounds} rounds! Final gold: {player.gold}.")
            
    
player = Player(name = "Alice", gold = 100)
game = MarbleGame()
game.run_round(player)
