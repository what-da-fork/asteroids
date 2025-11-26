# Asteroids

Simple single-player Asteroids-style game implemented in Python. The project includes game objects (asteroid, player, shots), game loop entry point, and simple tests.

## Features
- Asteroid field generation and movement
- Player ship with shooting mechanics
- Collision detection between shots, player, and asteroids
- Lightweight, easy-to-read code for learning and modification

## Requirements
- Python 3.8+
- Dependencies (if any) — check `pyproject.toml` or import statements in `main.py` (common: `pygame`)

Install typical dependency:
```bash
pip install pygame
```

## Run
Start the game from the repository root:
```bash
python main.py
```
If the project uses a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # if present
python main.py
```

## Controls
(Defaults — verify in `main.py` if different)
- Arrow keys: rotate / thrust the ship
- Space: fire
- R: restart
- Esc / close window: quit

## Testing
Run the included quick test script:
```bash
python test.py
```
For unit tests, inspect `test.py` and the game modules (`asteroid.py`, `player.py`, `shot.py`, `asteroidfield.py`, `circleshape.py`, `constants.py`) and adapt to your preferred test runner.

## Code structure
- main.py — entry point and game loop
- asteroid.py — asteroid behavior
- asteroidfield.py — manages collections of asteroids
- player.py — player ship logic and input handling
- shot.py — projectile behavior
- circleshape.py — circular collision / shape utilities
- constants.py — game constants and configuration
- test.py — quick tests / demo runner

## Contributing
- Open issues for bugs or feature requests
- Prefer small, focused PRs with clear descriptions

## Notes
- Intended as an educational / hobby project. Review and adapt controls and physics to suit gameplay preferences.
- Verify and install any missing dependencies listed in `pyproject.toml` or imported in `main.py`.

```// filepath: /home/m/workspace/github.com/what-da-fork/asteroids/README.md
# Asteroids

Simple single-player Asteroids-style game implemented in Python. The project includes game objects (asteroid, player, shots), game loop entry point, and simple tests.

## Features
- Asteroid field generation and movement
- Player ship with shooting mechanics
- Collision detection between shots, player, and asteroids
- Lightweight, easy-to-read code for learning and modification

## Requirements
- Python 3.8+
- Dependencies (if any) — check `pyproject.toml` or import statements in `main.py` (common: `pygame`)

Install typical dependency:
```bash
pip install pygame
```

## Run
Start the game from the repository root:
```bash
python main.py
```
If the project uses a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # if present
python main.py
```

## Controls
(Defaults — verify in `main.py` if different)
- Arrow keys: rotate / thrust the ship
- Space: fire
- R: restart
- Esc / close window: quit

## Testing
Run the included quick test script:
```bash
python test.py
```
For unit tests, inspect `test.py` and the game modules (`asteroid.py`, `player.py`, `shot.py`, `asteroidfield.py`, `circleshape.py`, `constants.py`) and adapt to your preferred test runner.

## Code structure
- main.py — entry point and game loop
- asteroid.py — asteroid behavior
- asteroidfield.py — manages collections of asteroids
- player.py — player ship logic and input handling
- shot.py — projectile behavior
- circleshape.py — circular collision / shape utilities
- constants.py — game constants and configuration
- test.py — quick tests / demo runner

## Contributing
- Open issues for bugs or feature requests
- Prefer small, focused PRs with clear descriptions

## Notes
- Intended as an educational / hobby project. Review and adapt controls and physics to suit gameplay preferences.
- Verify and install any missing dependencies listed in `pyproject.toml` or imported in `main.py`.
