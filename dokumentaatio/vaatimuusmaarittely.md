# Requirement specification

## Purpose of the app

The app is a version of the game Pong, where the user can configure settings such as game speed and how many balls are in play.

## Basic functionality

- Users can launch the game and play a version of Pong ✅
  - Settings are configured on the command line, after which the game launches ✅
    - Config file is saved ✅
- Stats are saved into a database ✅
  - The user can view their stats on the CLI ✅

## Extra features

- Customizability ✅
  - Users could change the color of their paddle or the ball, for example ✅
- Gameplay modifiers ✅
  - As mentioned above, users could change the parameters of the game in a multitude of ways:
    - Ball speed ✅
    - Paddle speed ✅
    - Amount of balls ✅
    - Difficulty of opponent AI ✅
- CLI UI has fancy colors, tables and text using Rich ✅

## Potential future features

- More settings to configure on the CLI
  - Paddle size
  - Ball size
  - Framerate
  - Game window size
- Additional game modes
  - Soccer(?)
  - More paddles
