# Cuber

A python program for many cubers out there.

## Installation

Clone the repository
```bash
git clone --recursive https://github.com/BijanRegmi/Cuber.git
```

Install the dependencies
```bash
cd Cuber
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

## Features
- Interactive 3D cube of nxn size
- Timer for recording cube solves
- Save and load your time records

## Controls
### For the 3D cube
Shortcut | Task
---------|------
X, Y, Z|Clockwise rotation of cube
Shift+(X, Y, Z)|Anti-clockwise rotation of cube
R, L, F, B, D, U|Cube moves in clockwise direction
Shift+(R, L, F, B, D, U)|Cube moves in anti-clockwise direction
Ctrl+R|Reset cube
Ctrl+V|Reset cube view
Ctrl+Shift+R|Reset cube and view
Ctrl+M|Toggle between manual rotation and auto rotation
Ctrl++|Increase cube order
Ctrl+-|Decrease cube order
+|Increase rotation speed
-|Decrease rotation speed

Also you can now rotate cube with mouse
- Right click for rotating along X and Y axis
- Left click for rotating along Z axis

### For the Timer
Shortcut | Task
---------|------
Space|Start or pause the timer
Return|Reset the timer
Del|Delete recorded time
R|Show cube solve history
Backspace|DNF the solve
+|Plus 2 on the time

## Future Goals
- Execute cube moves with mouse
- Official WCA scramble generator
- Camera input to read cube states
- Manual input to read cube state 
- Generate solution for a scrambled cube
- Pattern generator
- Algorithm grinders
