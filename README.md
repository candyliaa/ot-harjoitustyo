# Ohjelmistotekniikka: harjoitustyö

The app is a version of the game Pong, but with additional (perhaps even silly) game modifiers the user can control.

## Documentation

[Releases](https://github.com/candyliaa/ot-harjoitustyo/releases)

[Usage instructions](https://github.com/candyliaa/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Requirement specification](https://github.com/candyliaa/ot-harjoitustyo/blob/main/dokumentaatio/vaatimuusmaarittely.md)

[Work hours](https://github.com/candyliaa/ot-harjoitustyo/blob/main/dokumentaatio/workhours.md)

[Changelog](https://github.com/candyliaa/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[App architecture](https://github.com/candyliaa/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Installation instructions

1. (a) Download the latest [release](https://github.com/candyliaa/ot-harjoitustyo/releases).

1. (a) Alternatively, clone the repository to your machine:

```bash
git clone https://github.com/candyliaa/ot-harjoitustyo.git
```

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

Initializing / resetting the database:

```bash
poetry run build-db
```
