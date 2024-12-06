# Architecture description

## App structure

The app logic consists of classes that represent the basic Pong objects - Ball and Paddle - which the class Game uses to implement the game logic.
It also cotains a CLI UI, which is handled by the files in the `ui` directory, as well as a saved configuration, which the `config` object represents.

## UI
The UI consists of a main menu, which lets the user select from starting the game, viewing stats, configuring settings and exiting.
The stats display asks the user which type of stats to view - scores or misc. stats - and displays them accordingly.
The settings display asks the user which setting to change - such as paddle speed or ball color - and asks the user to make a choice, then updates the configuration accordingly.

## App logic
Individual components are split into their own directories, files, classes and methods. The `app.py` file then combines all of it and uses them when running the game in a loop.
Some examples of those components include:
- The UI files `cli_ui.py` and `console.py`
- The `repositories` directory which includes `stats_repository.py`, which is used to read from and write to the database
- The `sprites` directory which contains the relevant files and classes required for a game of Pong, those being `paddle.py` and `ball.py`.
Only `stats_repository.py` accesses the database, other files simply use the functions provided by the `StatsRepository` class within `stats_repository.py`.

## Saving data
The configuration for game modifiers is stored in the `config.json` file, which is used by the `config.py` file's `Config` class to read and update the config for each session.
Other data, such as how many times each player has scored, how many times the ball has bounced, total paddle travel distance, are stored in `data.db`, and accessed by `stats_repository.py`. This data can be viewed on the CLI: `cli_ui.py` handles that with the `Stats` class.
Specifically, the data in the database is stored in the following tables:
Table `scores`, which contains columns `session, scored, scored_on`; first value being the session no., second value the amount of times the player scored, and the third the amount of times the player was scored on.
Also table `misc`, which contains columns `session, ball_bounces, own_paddle_traveled, enemy_paddle_traveled`, which contain data similarly as in `scores`. The data is then read and summed so that the user can see the totals of those values.

## Possible improvements
As it is now, `app.py` is quite large and could possibly be split into smaller files and / or classes. On the other hand, having the game logic in one class makes it easier to read the flow of the events.

![image](https://github.com/user-attachments/assets/12b3e4d5-c296-4491-97bb-1b0816b2e0c8)


# Sequence diagram
![image](https://github.com/user-attachments/assets/b57ed777-03d8-4e85-bff6-d80f0994dfc3)

The individual components are initialized before starting the game.
