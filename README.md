# Galaxy Figther
This in Astroids-like game that pits the player ships against enemy ships and will use a rotary encoder to handle the controls.

## Development
- Language - Python 3.7.3
- Platform - Raspberry Pi 3 B+
- OS - Rasbian 4.19 "Buster"
- Environment - CodeOSS (headmelted) 1.29.0

## Modules
- RPi
- PyGaqme

## Goals
- [X] Get rotary encoder working (Used Sunfounder Senser Kit v2.0 for Raspberry Pi B+ code - Lesson 27)
- [X] Use a triangle to represent the ship and rotate it
- [X] Get a bullet to move from player in a straight line to the edge of the screen - Had to use https://github.com/bandali0/asteroids game as an example
- [X] Use rectangles to represent the enemy ships
- [X] Get collision between bullets and the enemy ships
- [X] Move enemy units
- [X] Have enemy units move toward player in an arc
- [ ] Draw Sprite for player ship to screen  -- Might descope sprites for now
- [x] Get ship to rotate and fire with keyboad keys
- [ ] Draw Sprites for enemy ship to screen  -- Might descope sprites for now
- [x] Get multiple enemy ships to screen
- [ ] Clean up code to make it pretty