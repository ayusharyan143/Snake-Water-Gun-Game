# Snake-Water-Gun Game

A simple command-line Snake-Water-Gun game written in Python.

## Game Rules

1. Snake (s) beats Water (w)
2. Water (w) beats Gun (g)
3. Gun (g) beats Snake (s)
4. If both the player and the computer choose the same option, it's a tie.

## How to Play

1. The computer will randomly choose Snake, Water, or Gun.
2. You will be prompted to enter your choice: `s` for Snake, `w` for Water, or `g` for Gun.
3. The game will determine the winner based on the rules above.

## Running the Game

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the game script.
4. Run the game script using the following command:

    ```sh
    python snake_water_gun.py
    ```

5. Enter your choice when prompted.

## Example

```sh
$ python snake_water_gun.py
Enter your choice (s for Snake, w for Water, g for Gun): s
Computer chose: Water
You chose: Snake
You Win!
