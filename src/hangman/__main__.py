from .game import GameSession


class TerminalPlayer:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, KeyboardInterrupt):
            print("Thanks for playing")
            return True

    def render_game(self, session, game, last_success=None):
        state = " ".join(["_" if l is None else l.upper() for l in game.state])
        to_render = [state]
        if not game.finished:
            to_render.append(f"attempts left: {game.attempts_left}")
        elif last_success:
            to_render.append("Congratulations")
            to_render.append(f"Highest score: {session.high_score}")
        else:
            to_render.append("Game Over")
        print(", ".join(to_render))

    def get_input(self):
        while True:
            result = input("Enter a letter and press ENTER: ")
            if len(result) != 1:
                print("Please enter a single letter")
            else:
                break
        return result

    def ask_continue(self) -> bool:
        try:
            input('Press Enter to continue, Ctrl+C to exit')
            return True
        except KeyboardInterrupt:
            return False


def main(words=None, player=None):
    session = GameSession(words) if words else GameSession.with_default_words()
    player = TerminalPlayer() if player is None else player
    with player:
        while True:
            game = session.new()
            player.render_game(session, game)
            while True:
                letter = player.get_input()
                success = game.play(letter)
                player.render_game(session, game, last_success=success)
                if game.finished:
                    break
            if player.ask_continue():
                continue
            else:
                break


if __name__ == '__main__':
    main()
