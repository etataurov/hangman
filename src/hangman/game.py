import collections
import random
from typing import List, Optional, Dict, Callable, Any

DEFAULT_WORDS = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']


class GameSession:
    """
    Creates new games and keep track of highest score
    """
    def __init__(
        self,
        words: List[str]
    ):
        self._high_score = 0
        self.words = words

    def __repr__(self):
        return f"GameSession<high_score={self.high_score}>"

    @classmethod
    def with_default_words(cls) -> 'GameSession':
        return cls(DEFAULT_WORDS)

    @property
    def high_score(self) -> int:
        return self._high_score

    def new(self) -> 'Game':
        """
        Create a new game with random word
        """
        return Game(
            word=random.choice(self.words),
            on_game_finished=self._update_high_score,
        )

    def _update_high_score(self, game: 'Game'):
        if game.score > self._high_score:
            self._high_score = game.score


class Game:
    MAX_SCORE = 100
    ATTEMPTS = 5

    def __init__(
        self,
        word: str,
        on_game_finished: Optional[Callable[['Game'], Any]] = None,
    ):
        self.__word = word
        self._state: List[Optional[str]] = [None] * len(word)
        self._attempts_left = self.ATTEMPTS
        self._index = self._build_index(word)
        self._on_game_finished = on_game_finished

    def __repr__(self):
        return f"Game<{self.state}, finished={self.finished}, attempts_left={self.attempts_left}>"

    @property
    def attempts_left(self) -> int:
        return self._attempts_left

    @property
    def state(self) -> List[Optional[str]]:
        """
        Current game state
        Guessed letters represented as letters
        None indicates not guessed letter
        """
        return self._state.copy()

    @property
    def score(self) -> int:
        """
        Score gained in the game
        """
        return self.MAX_SCORE * self._attempts_left // self.ATTEMPTS

    @property
    def finished(self) -> bool:
        return not self._attempts_left or None not in self._state

    @staticmethod
    def _build_index(word) -> Dict[str, List[int]]:
        letter_index = collections.defaultdict(list)
        for index, letter in enumerate(word):
            letter_index[letter.lower()].append(index)
        return letter_index

    def play(self, letter: str) -> bool:
        """
        Play the letter,
        Resulting bool indicates whether the guess was correct or no
        """
        if self.finished:
            raise RuntimeError("Game finished")
        if len(letter) != 1:
            raise ValueError(f"Provided: {letter}, expected single letter")
        indices = self._index.get(letter.lower())
        if not indices:
            self._attempts_left -= 1
            correct = False
        else:
            correct = True
            for index in indices:
                self._state[index] = letter
        if self._on_game_finished and self.finished:
            self._on_game_finished(self)
        return correct
