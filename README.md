# Word_Raider_Game
A terminal-based Wordle-style word guessing game built in Python with colored feedback and game statistics.

#  Word Raider - Python Word Guessing Game

Word Raider is a terminal-based word guessing game inspired by Wordle.  
Your mission is simple: **Guess the 5-letter word in 6 attempts!**

---

##  How the Game Works

- You get **6 chances** to guess a random 5-letter word.
- After each guess, you receive colored feedback:

| Color | Meaning |
|--------|----------|
| 🟩 Green | Correct letter in correct position |
| 🟨 Yellow | Correct letter in wrong position |
| ⬜ Gray | Letter not in the word |

---

## 🚀 Features

-  Colored terminal output (ANSI colors)
-  Replay option after each game
- Game statistics tracking  
- Games Played  
- Games Won  
- Win Rate %
- Smart duplicate letter handling
- Input validation (only 5 letters allowed)

---

##  Technologies Used

- Python 3
- Random module
- OS module (for clearing terminal)
- ANSI escape sequences (for colors)

---

## ▶️ How to Run the Game

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/word-raider-python.git
```

### 2️⃣ Navigate to the project folder

```bash
cd word-raider-python
```

### 3️⃣ Run the game

```bash
python word_raider.py
```

---

##  Project Structure

```
word-raider-python/
│
├── word_raider.py
└── README.md
```

---

##  Example Gameplay

```
Attempt 1/6
 A P P L E
 B R A I N
```

Green, Yellow, and Gray colors guide you to the correct word!

---

##  Future Improvements

- Larger word database
- Difficulty levels
- Timer mode
- Save high scores
- GUI version (Tkinter or Pygame)
- Web version (Flask / Django)

---

##  Contributing

Pull requests are welcome!  
If you find a bug or have suggestions, feel free to open an issue.

---

##  License

This project is open-source and available under the MIT License.

---

##  Author

**Abhishek Rawat**  
Aspiring Data Analyst


