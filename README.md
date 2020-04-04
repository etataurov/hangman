# Hangman

## Install
```bash
python setup.py install
```

## Run
```bash
3dhangman
```

## Development

```bash
pip install -e ".[dev]"
```

### Run tests

```bash
pytest
```

## Play via Python API

```
>>> from hangman import GameSession
>>> session = GameSession.with_default_words()
>>> game = session.new()
>>> game.play('b')
False
>>> game.play('o')
True
>>> game
Game<['o', None, None, None, None], finished=False, attempts_left=4>
```