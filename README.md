# 🧩 Mosaic Browsing – PyGame

Mosaic Browsing is a GUI-based pattern recognition game built with **Python and Tkinter**, where players search for a hidden color motif embedded inside a dynamically generated mosaic grid.

---

## 🎮 Game Overview

The game presents:
- A **10×10 mosaic grid** with randomly colored cells
- A **2×2 motif** displayed separately
- The motif is secretly embedded somewhere inside the mosaic

The player must visually inspect the mosaic, select a 2×2 region, and verify whether it matches the given motif.

---

## ✨ Features

- 🎨 Randomly generated colorful mosaic and motif
- 🧠 Pattern recognition and visual reasoning gameplay
- 🔊 Sound effects and background music using **pygame**
- 🖱️ Interactive mouse-based selection
- ⭐ Score tracking system
- 🔁 Restart and ❌ Exit controls
- 🖥️ Fullscreen animated welcome screen

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** – GUI framework
- **Pygame** – sound effects & background music
- **Random** – grid and motif generation

---

## 📜 Game Rules

1. The mosaic is a **10×10 grid** of randomly colored cells.
2. The motif is a **2×2 grid** of randomly colored cells.
3. The motif is hidden at a random position inside the mosaic.
4. Click on any **2×2 region** in the mosaic to select it.
5. Press **Find Motif** to check for a match.
6. ✅ Correct match → score increases.
7. ❌ Wrong match → correct motif location is highlighted.
8. Restart anytime to generate a new puzzle.

---
## 📂 Project Structure

```text
mosaic-browsing-PyGame/
│
├── mosaic-browsing_final.py   # Main game file
├── motif_test.py              # Motif testing logic
├── wiseproject.py             # Supporting logic
├── *.mp3 / *.wav              # Sound effects & music
├── mosaic_pic1.jpg            # Game image asset
├── README.md                  # Project documentation
└── pyvenv.cfg                 # Virtual environment config
```
---

## ▶️ How to Run the Game

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sirichandana17/mosaic-browsing-PyGame.git
cd mosaic-browsing-PyGame
```
### 2️⃣ Install Dependencies
```bash
pip install pygame
```
### 3️⃣ Run the Game
```bash
python mosaic-browsing_final.py
```
---
## 👩‍💻 Author

**Siri Chandana Kanaparthi**  
