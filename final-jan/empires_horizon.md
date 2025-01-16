# Empires Horizon

Empires Horizon is a resource management game in which players explore the Eastern Woodlands and manage resources such as meat, stone, wood, water, and population. The goal is to win by strategically gathering resources, constructing buildings, and ensuring survival.

---

## Features

- **Explore:** Navigate through the Eastern Woodlands to manage resources.
- **Resource Management:** Collect, consume, and strategize with meat, stone, wood, water, and population.
- **Dynamic Events:** Random events affect your resource collection.
- **Win or Lose:** Achieve victory by gathering enough resources or face defeat if resources are depleted.

---

## Requirements

- **Python Environment:** Python 3
- **SimpleGUI Module:** The game uses the SimpleGUI library, part of the CodeSkulptor platform. Visit CodeSkulptor3 to run this game

## How to Play

### Start the Game:
Run the Python file in CodeSkulptor3.

### Game Controls:
- **Hunt:** Collect or lose meat based on random events.
- **Mine:** Gather or lose stone through mining actions.
- **Logging:** Chop wood or face setbacks in the woods.
- **Population:** Manage your population through growth and loss events.
- **Build:** Construct a well when you have sufficient resources.
- **Collect Water:** Gather water from the well after it's built.

### Win or Lose Conditions:
- **Win:** Collect at least 100 units of each resource and reach a population of 50.
- **Lose:** Deplete all resources and population.

## Game Screens

- **Menu Screen:** Displays the game title and resource overview.
- **Eastern Woodlands:** Interactive gameplay area for resource management.

## Commands

Use the following in-game commands:
- `hunt()`: Hunt for meat.
- `mine()`: Gather stone.
- `logging()`: Collect wood.
- `population()`: Build a population.
- `build()`: Construct a well.
- `well()`: Collect water after building the well.

## Code Structure

- **Images:** Image assets for visual elements.
- **Resources:** Tracks resource levels and interactions.
- **Screens:** Handles the menu and gameplay screens.
- **Actions:** Functions for hunting, mining, logging, population management, and building.
