from hangman import GameSession


def test_game_session():
    session = GameSession(
        words=['test']
    )
    assert session.high_score == 0


def test_game():
    session = GameSession(
        words=['test']
    )
    game = session.new()
    assert game.state == [None, None, None, None]
    assert game.attempts_left == 5
    assert game.play('t')
    assert game.state == ['t', None, None, 't']
    assert game.score == 100
    assert not game.finished
    assert game.play('e')
    assert game.play('s')
    assert game.score == 100
    assert game.finished


def test_game_failure():
    session = GameSession(
        words=['test']
    )
    game = session.new()
    assert game.state == [None, None, None, None]
    assert game.attempts_left == 5
    assert not game.play('a')
    assert game.state == [None, None, None, None]
    assert game.score == 80
    assert not game.finished
    assert not game.play('b')
    assert not game.play('c')
    assert not game.play('d')
    assert not game.play('d')
    assert game.score == 0
    assert game.finished


def test_session_high_score_updated():
    session = GameSession(
        words=['x']
    )
    game = session.new()
    assert session.high_score == 0
    game.play('x')
    assert session.high_score == 100
