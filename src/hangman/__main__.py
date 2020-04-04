from .main import GameSession


class TerminalPlayer:
    def render_game(self, game):
        state = " ".join(["_" if l is None else l.upper() for l in game.state])
        print(f"{state}, attempts left: {game.attempts_left}")

    def get_input(self):
        result = input("Enter a letter: ")
        return result

    def render_correct(self):
        print("Correct")

    def render_incorrect(self):
        print("Incorrect")

    def render_highscore(self, score):
        print(f"Highest score: {score}")

    def ask_continue(self) -> bool:
        try:
            input('Continue?')
            return True
        except KeyboardInterrupt:
            return False

    def render_close(self):
        print("Thanks for playing")


def main():
    words = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']
    session = GameSession(words)
    player = TerminalPlayer()
    while True:
        game = session.new()
        while True:
            player.render_game(game)
            let = player.get_input()
            if game.play(let):
                player.render_correct()
            else:
                player.render_incorrect()
            if game.finished:
                break
        player.render_highscore(session.high_score)
        if player.ask_continue():
            continue
        else:
            break
    player.render_close()


if __name__ == '__main__':
    main()
