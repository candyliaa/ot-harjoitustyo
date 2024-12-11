# Changelog

## Week 3

- Created base for Pong game
- Pong objects are located in the `sprites` directory, where each file corresponds to an object
- Tests for paddle movement added in `paddle_test.py` file

## Week 4

- Implemented functional Pong game
- Improved logic of classes Ball and Paddle by refactoring
- Tests for ball movement added in `paddle_test.py` file
- Refactored `app.py` to use a `Game` class

## Week 5

- Implemented CLI UI before launching the game itself
  - This lets the user configure a variety of settings
- Refactored code to accommodate for CLI
- Config is saved to the `config.json` file

## Week 6

- Implemented database to store game stats in
  - Also implemented a stats repository which reads from and writes to the database
- Implemented the stats page of the CLI UI, which lets the user view stats in a neat format
- Wrote tests for the database

## Week 7

- Implemented the option to add multiple balls to the game
- Made the CLI look nicer with proper linebreaks, error messages and the usage of the Rich library
  - Multiple things are color-coded
  - Stats can be viewed in a neat table
- Wrote more tests for settings
- Refactored code slightly by adding the `_` prefix to variables that only the respective class uses
  - Also changed some game logic to account for multiple balls
- Updated documentation
