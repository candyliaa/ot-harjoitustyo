# Ohjelmistotekniikka: harjoitustyö

The app is a version of the game Pong, but with additional (perhaps even silly) game modifiers the user can control.

## Documentation

[Requirement specification](https://github.com/candyliaa/ot-harjoitustyo/blob/main/dokumentaatio/vaatimuusmaarittely.md)

[Work hours](https://github.com/candyliaa/ot-harjoitustyo/blob/main/dokumentaatio/workhours.md)

[Changelog](https://github.com/candyliaa/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[App architecture](https://github.com/candyliaa/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Installation instructions

1a. Clone the repository to your machine:

```bash
git clone https://github.com/candyliaa/ot-harjoitustyo.git
```

1b. Alternatively, download the latest release.

2. In the root directory of the project, run

```bash
poetry install
```

3. Build the database with

```bash
poetry run invoke build-db
```

4. Run the app with

```bash
poetry run invoke start
```

## CLI commands

All of these should be ran in the root directory of the project (not in src!)

Running the app:

```bash
poetry run invoke start
```

Running the tests:

```bash
poetry run invoke test
```

Test coverage report:

```bash
poetry run invoke coverage-report
```

Pylint code quality report:

```bash
poetry run invoke lint
```
