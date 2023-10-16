import typing
import random


class Game:
    def __init__(self, score=100):
        self.score = score

    def start_game(self):
        decrement = 10
        result = random.randint(0, 100)
        count_hints = self.score // 10

        while self.score > 0:
            user_input = input("Please make a guess:")
            if int(user_input) == result:
                print(f"Nice guess: {user_input} is correct, score {self.score}")
                return 0
            elif count_hints > 0:
                self.score -= 10
                count_hints -= 1
                hint_range = random.randint(0, 9)
                result_lower_bound = result - hint_range
                result_upper_bound = result + hint_range
                print(
                    f"The guess is incorrect, the number is somewhere between {result_lower_bound} and {result_upper_bound} "
                    f"Current score: {self.score}")
            else:
                print("You lose")

newgame = Game()
newgame.start_game()