//AP21110010177//

def create(initial_state, level):
    def is_valid_move(x, y):
        return 0 <= x < 3 and 0 <= y < 3

    def swap_tiles(state, x1, y1, x2, y2):
        new_state = [row[:] for row in state]
        new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
        return new_state

    def print_state(state, current_level):
        print("Level:", current_level)
        for row in state:
            print(row)
        print()

    def generate_next_states(current_state, current_level):
        if current_level > level:
            return

        x, y = None, None

        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    x, y = i, j
                    break

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y):
                new_state = swap_tiles(current_state, x, y, new_x, new_y)
                print_state(new_state, current_level)
                generate_next_states(new_state, current_level + 1)

    generate_next_states(initial_state, 1)
