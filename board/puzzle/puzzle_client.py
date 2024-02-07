import requests
import random


class PuzzleClient:
    def __init__(self):
        self.client = requests.Session()
        self.total_puzzles = 28261

    def get_puzzle(self):

        random_digit = random.randint(1, self.total_puzzles - 1)

        response = self.client.get(
            f"https://pychess.run.goorm.io/api/puzzle?limit=1&offset={random_digit}"
        )
        puzzle_id = response.json().get("items")[0].get("puzzleid")

        move = self.client.get(
            f"https://pychess.run.goorm.io/api/puzzle/move?puzzleid={puzzle_id}"
        )

        return move.json()
