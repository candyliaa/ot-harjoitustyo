# Usage instructions

First, download the latest release (or follow the instructions in the `README` file).

## Running the app

Before running the app, install the required dependencies using

```bash
poetry install
```

After which run

```bash
poetry run invoke build-db
```

to build the database.

The app can then be started with

```bash
poetry run invoke start
```

## UI

Upon launching the application, it opens in a text-based UI.The main menu shows the possible options for the user. The user then has to input the corresponding number and hit the enter key to proceed.

## Configuration

The configuration of the game can be changed by accessing the Settings menu from the main menu, by inputting `3`. The user is then presented with a variety of options, and has to choose from them, and give updated values if the user wishes to.

## Stats

To view stats for the game, the user can access the Stats menu from the main menu, by inputting `2`. The user is again presented with options to choose from, so that they can view the stats they wish to.

## Playing the game

To launch the game and to start playing Pong, simply launch the application, and input `1` in the main menu. This opens the game window and lets the user control a paddle to bounce the ball off of.
