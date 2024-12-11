# Testing document

The application is largely covered by unittests and manual tests to ensure it won't break.

## Unittests

### Settings

All possible settings options are tested with unittests, and invalid inputs are also covered. This is done in `settings_test.py` with the `TestSettings` class. To do this, there's also a `MockIO` class present which is used to simulate inputs on the CLI to test the wanted features.

### Database

The database connection and write/read functions are tested in `stats_repository_test.py` with the `TestStatsRepository` class. The tests check if the required tables exist, and also if data is written to the database and read from it correctly.

### Game objects

Various tests for the game logic of Pong game objects (namely `Ball` and `Paddle`) are present. They test various movement related properties of both objects.
Specifically for the ball, the tests test that:
    - The ball bounces off of the "floor" and "ceiling" of the game window
    - The ball is scored when it touches the left or right edge of the game window
    - The ball starts at and resets to the correct position
And for the paddle:
    - The paddle can't go out of bounds
    - The paddle spawns in the correct position
    - The user's paddle moves the correct amount on user input

## System testing

The app has been tested on Windows and Cubbli Linux. All kinds of usecases related to configuration are tested, such as when the database tables do not exist and when configuration isn't set. The tests cover the requirement specification's list of features.