from typing import List, Optional
import random
import collections


class GameSession:
    def __init__(
            self,
            words: List[str]
    ):
        self._high_score = 0
        self.words = words

    @property
    def high_score(self):
        return self._high_score

    def _update_high_score(self, game: 'Game'):
        if game.score > self._high_score:
            self._high_score = game.score

    def new(self) -> 'Game':
        return Game(
            word=random.choice(self.words),
            on_game_finished=self._update_high_score,
        )


class Game:
    MAX_SCORE = 100

    def __init__(
            self,
            word: str,
            on_game_finished = None,
            attempts: int = 5
    ):
        self.__word = word
        self._state = [None] * len(word)
        self._total_attempts = attempts
        self._attempts = attempts
        self._index = self._build_index(word)
        self._on_game_finished = on_game_finished

    @property
    def attempts_left(self) -> int:
        return self._attempts

    @property
    def state(self) -> List[Optional[str]]:
        return self._state.copy()

    @property
    def score(self) -> int:
        return self.MAX_SCORE * self._attempts // self._total_attempts

    @property
    def finished(self) -> bool:
        return not self._attempts or None not in self._state

    @staticmethod
    def _build_index(word):
        letter_index = collections.defaultdict(list)
        for index, letter in enumerate(word):
            letter_index[letter.lower()].append(index)
        return letter_index

    def play(self, letter: str) -> bool:
        if self.finished:
            raise RuntimeError("Game finished")
        if len(letter) != 1:
            raise ValueError(f"Provided: {letter}, expected single letter")
        indices = self._index.get(letter.lower())
        if not indices:
            self._attempts -= 1
            if self._on_game_finished and self.finished:
                self._on_game_finished(self)
            return False
        for index in indices:
            self._state[index] = letter
        if self._on_game_finished and self.finished:
            self._on_game_finished(self)
        return True

