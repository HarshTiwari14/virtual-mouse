# Virtual Mouse 🎯

## Overview  
This project enables controlling your computer’s mouse using hand-gestures (and optionally other input modes). Using a webcam and computer vision libraries, you can move the cursor, click, scroll and perform basic mouse operations without a physical mouse.

The goal is to offer a touchless, intuitive interaction method — useful for accessibility, presentations, or just fun experiments.

## Features  
- Real-time hand tracking using webcam  
- Move the cursor by pointing with finger(s)  
- Left-click, right-click, double-click via gesture combinations  
- Scrolling (vertical/horizontal) using gesture motion  
- (Optional) Additional actions: drag & drop, volume/brightness control, etc.  
- Easily extendable for custom gestures or new control types  

## Tech Stack  
- Python (3.x)  
- Libraries: OpenCV, MediaPipe (or a similar hand-tracking library), PyAutoGUI (or OS mouse control)  
- Git / GitHub for version control  

## Getting Started  

### Prerequisites  
- Python 3.7+ (some dependencies may require 3.8)  
- Webcam connected and accessible  
- `pip` or `conda` package manager  

### Installation  
1. Clone the repo  
   ```bash
   git clone https://github.com/HarshTiwari14/virtual-mouse.git
   cd virtual-mouse
