# 🎯 Number Guessing Game

A professional and interactive **Number Guessing Game** built with **Python** and **Streamlit**.

The player selects a difficulty level and tries to guess a randomly generated secret number. The application provides helpful higher/lower hints, tracks attempts, and displays the player's guess history.

## 🎮 Difficulty Levels

| Level | Number Range |
|---|---|
| Easy | 1–10 |
| Medium | 11–50 |
| Hard | 51–100 |

Changing the difficulty automatically starts a new game using the selected range.

## ✨ Features

- Three difficulty levels
- Random secret number generation
- Higher and lower hints
- "Very close" hints when near the correct answer
- Attempt counter
- Guess history
- Dynamic number range
- New Game button
- Success message and balloon animation
- Clean and responsive Streamlit interface
- Custom styling
- Streamlit session state for game progress

## 📁 Project Structure

```text
number-guessing-game/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Make sure Python is installed on your computer.

Clone or download the project and open a terminal inside the project folder.

Install the required package:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

Streamlit will start the application and open it in your web browser.

## 🕹️ How to Play

1. Select a difficulty level.
2. Enter a number within the displayed range.
3. Click **Submit Guess**.
4. Read the hint:
   - **Too low** → choose a higher number.
   - **Too high** → choose a lower number.
   - **Very close** → your guess is near the secret number.
5. Continue guessing until you find the correct number.
6. Click **Start New Game** to generate another secret number.

## 🧠 Game Logic

The application uses Python's `random.randint()` function to generate a secret number within the selected difficulty range.

For example:

```python
secret_number = random.randint(min_val, max_val)
```

Streamlit's `st.session_state` is used to preserve:

- Selected difficulty
- Secret number
- Number of attempts
- Guess history
- Game status
- Feedback messages

## 🚀 Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. Sign in to Streamlit Community Cloud.
4. Select your GitHub repository.
5. Set `app.py` as the main application file.
6. Deploy the app.

## 📦 Requirements

The `requirements.txt` file only needs:

```text
streamlit
```

The Python `random` module does not need to be installed because it is included with Python.

## 🛠️ Technologies Used

- Python
- Streamlit
- HTML/CSS for custom Streamlit styling

## 📌 Notes

No machine-learning model or `.pkl` file is required for this project. The secret number is generated directly by Python.

---

### 🎯 Number Guessing Game

Built with Python and Streamlit.
