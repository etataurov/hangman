from unittest import mock

from hangman.__main__ import main


def test_played():
    words = ['test']
    player_instance = mock.MagicMock()
    player = player_instance.__enter__.return_value
    player.ask_continue.return_value = False
    player.get_input.side_effect = ['t', 'e', 's']

    main(words, player)

    render_calls = player.render_game.call_args_list
    assert len(render_calls) == 4
    game = render_calls[-1][0][1]
    assert game.finished

    assert player.get_input.call_count == 3
    assert player.ask_continue.call_count == 1


def test_played_incorrect_guesses():
    words = ['test']
    player_instance = mock.MagicMock()
    player = player_instance.__enter__.return_value
    player.ask_continue.return_value = False
    player.get_input.side_effect = ['t', 'd', 'r', 'e', 's']

    main(words, player)

    render_calls = player.render_game.call_args_list
    assert len(render_calls) == 6
    game = render_calls[-1][0][1]
    assert game.finished
    assert game.attempts_left == 3

    assert player.get_input.call_count == 5
    assert player.ask_continue.call_count == 1


def test_continue_playing():
    words = ['test']
    player_instance = mock.MagicMock()
    player = player_instance.__enter__.return_value
    player.ask_continue.side_effect = [True, False]
    player.get_input.side_effect = ['t', 'e', 's', 't', 'e', 's']

    main(words, player)

    render_calls = player.render_game.call_args_list
    assert len(render_calls) == 8

    assert player.get_input.call_count == 6
    assert player.ask_continue.call_count == 2
