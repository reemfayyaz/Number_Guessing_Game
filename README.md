# 🎯 Number Guessing Game

A simple and professional **Number Guessing Game** built with Python and Streamlit.

The application generates a random number between **1 and 10**. The player enters a guess, and the app provides hints until the correct number is found.

## Features

- Clean Streamlit user interface
- Random number generation
- High/low hints
- Attempt counter
- Guess history
- New Game button
- Success animation
- Easy to deploy on Streamlit Community Cloud

## Project Files

```text
number-guessing-game/
├── app.py
├── requirements.txt
└── README.md
```

## Installation

1. Download or clone the project.
2. Open a terminal in the project folder.
3. Install the required package:

```bash
pip install -r requirements.txt
```

## Run the App

Run:

```bash
streamlit run app.py
```

Streamlit will open the application in your web browser.

## Deploy on Streamlit Community Cloud

1. Upload `app.py`, `requirements.txt`, and `README.md` to a GitHub repository.
2. Sign in to Streamlit Community Cloud.
3. Select your GitHub repository.
4. Choose `app.py` as the main file.
5. Deploy the application.

## Requirements

- Python 3.9 or newer
- Streamlit

## How to Play

Enter a number from **1 to 10** and click **Submit Guess**.

- If your guess is too low, the app asks you to try a higher number.
- If your guess is too high, the app asks you to try a lower number.
- If your guess is correct, you win.

Click **Start New Game** to play again.

## Technology

- Python
- Streamlit

---

Built with Python and Streamlit.
