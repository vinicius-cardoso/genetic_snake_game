from game import Game

snake_body_list = [
    [
        [20, 400],
        [20, 410],
        [20, 420]
    ],
    [
        [20, 390],
        [20, 400],
        [20, 410]
    ],
    [
        [20, 380],
        [20, 390],
        [20, 400]
    ],
    [
        [20, 370],
        [20, 380],
        [20, 390]
    ],
    [
        [20, 360],
        [20, 370],
        [20, 380]
    ],
    [
        [20, 350],
        [20, 360],
        [20, 370],
        [20, 380]
    ],
    [
        [20, 340],
        [20, 350],
        [20, 360],
        [20, 370]
    ]
]

fruit_positions_list = [
    [20, 350],
    [20, 350],
    [20, 350],
    [20, 350],
    [20, 350],
    [100, 400],
    [100, 400]
]

frames = (snake_body_list, fruit_positions_list)

if __name__ == "__main__":
    game = Game()
    game.draw_game(frames)
